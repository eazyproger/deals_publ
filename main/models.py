from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=20)
    spent_money = models.IntegerField(auto_created=0)
    gems = models.TextField(auto_created='')

    def __str__(self):
        return str(self.username) + ' ' + str(self.spent_money) + ' ' + str(self.gems)


class Deal(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    item = models.CharField(max_length=20)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()


class Stone(models.Model):
    name = models.CharField(max_length=20)
