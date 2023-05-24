# Dark_forest-server

![GitHub forks](https://img.shields.io/badge/Version-1.0-red)

Django Server for Dark Forest game, integrate with Dark Forest client

Now you can create account,login to account,show globals scores and stats.

MySQL server is required (I use mariadb)

Install libs: pip install -r requirements.txt

create .env like .env.example to configure server

Qwizi create Docker-compose for this server and hosting server<3

In main folder type docker-compose up to run it

In main django folder type in cmd:

python manage.py make migrations

python manage.py migrate

To run type:

python manage.py runserver

Description:

Stats is a main django folder

I prefer pytest so I configure django from pytest

In main django folder is another stats folder, this is a server

In Settings I configure app for this project

In urls I add path to app

in main django folder is a folder named stats_server, this is a app

In migrations i have my database migrations

In templates folder i have templates for login and register because I use csrf

In Test folder i have unit tests

In admin i create admin panel to my models

In models i define data models to database, stats and best scores are in apart tables

In urls i have paths from views

In views i have my endpoints to communicate with client
