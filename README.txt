Веб-сервис deals

ссылка на сервер с проектом: https://polar-beach-55113.herokuapp.com/

Загрузите приложение с этого репозитория

Для запуска на локальном сервере необходимо перейти в директорию проекта, затем использовать команду: 
	python manage.py runserver

Для запуска на сервере heroku
	Если вы сделали какие-либо изменения:
		git commit -m 'описание'
		git push heroku master
	Далее:
	heroku run python manage.py runserver
	Использойте heroku open для перехода к сервису
	
Использование:
Приложение реализует интерфейс restapi
для получения response использует метод GET
для загрузки файла со сделками использует метод POST, с параметром
	form-data key=file value=<файл>

Для тестирования приложения использовалось приложение POSTMAN

Плюсы приложения: используется DRF
Минусы приложения: не используется docker из-за технических проблем разработчика
