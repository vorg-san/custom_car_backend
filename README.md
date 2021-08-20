# NFT Vision Hackathon



## Setup

1) Create Mysql instance and run 'create database custom_car;'
2) Set enviroment variables:
	- 'DJANGO_CUSTOM_CAR_SECRET_KEY' - random secret string 
	- 'MYSQL_USER' - mysql database user
	- 'MYSQL_PASS' - mysql database password
	- 'MYSQL_HOST' - mysql database url
3) Clone repo
4) cd into cloned repo folder
	- add your server ip to settings.py, for example: ALLOWED_HOSTS = ['44.196.172.48']
	- pip install Django django-cors-headers djangorestframework
5) run: python manage.py migrate
6) run: python manage.py loaddata initialdb
7) run: python manage.py runserver 0.0.0.0:8001

