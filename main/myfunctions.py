import csv
from datetime import datetime
from .models import Deal, Customer, Stone


class IncorrectField(Exception):
    pass


class Ok(Exception):
    pass


def check_correctness_file(filename):
    with open(filename, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            if int(row['total']) <= 0:
                raise IncorrectField("Некоректное поле 'total': " + row['total'])
            if int(row['quantity']) <= 0:
                raise IncorrectField("Некоректное поле 'quantity': " + row['total'])
            datetime.strptime(row['date'], "%Y-%m-%d %H:%M:%S.%f")
    upload_into_db(filename)


def upload_into_db(filename):
    with open(filename, encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            customers = Customer.objects.all()
            this_customer = None
            for customer in customers:
                if row['customer'] == customer.username:
                    customer.spent_money += int(row['total'])
                    customer.save()
                    this_customer = customer
                    this_customer.save()
                    break
            if this_customer is None:
                this_customer = Customer(username=row['customer'], spent_money=0)
                this_customer.save()
            deal = Deal(
                customer=this_customer,
                item=row['item'],
                total=row['total'],
                quantity=row['quantity'],
                date=row['date']
            )
            deal.save()
            stone = Stone.objects.filter(name=deal.item)
            if stone.count() == 0:
                new_stone = Stone(name=deal.item)
                new_stone.save()
    update_gems()
    raise Ok()


def update_gems():
    for deal in Deal.objects.all():
        if deal.customer in get_top() and str(deal.customer.gems).find(deal.item) == -1:
            deal.customer.gems = str(deal.customer.gems) + ' ' + str(deal.item)
            deal.customer.save()

    for top_customer in get_top():
        stones = str(top_customer.gems).split()
        top_customer.gems = ''
        top_customer.save()
        for stone in stones:
            for top_customer2 in get_top():
                if str(top_customer2.gems).find(stone) != -1:
                    top_customer.gems = str(top_customer.gems) + ' ' + str(stone)
        top_customer.save()


def get_top():
    top = Customer.objects.order_by('-spent_money')
    top5 = top[:5]
    return top5