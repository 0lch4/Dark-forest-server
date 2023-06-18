# Dark Forest Server ![GitHub forks](https://img.shields.io/badge/Version-1.0.0-red)

# Description

Django Server for Dark Forest game, integrate with Dark Forest client

This server is already running in internet, here I set values for localhost. To connect to server use [Dark Forest client on localhost values](https://github.com/0lch4/Dark_forest_client/blob/version_for_localhost/README.md)

## License

Application is licensed under the MIT License.

# Instalation

[MySQL](https://dev.mysql.com/downloads/mysql/) server is required.

## Copying the repository

```
git clone https://github.com/0lch4/Dark-forest-server.git
```

## Installing liblaries

You have to use poetry to install liblaries:

```
pip install poetry
```

In next step enter in main project location:

```
poetry install
```

Finally, activate your environment:

```
poetry shell
```

## .env file

You have to create `.env` like `.env.example`

# Usage

When all dependencies are met, enter in the main django location:

```
python manage.py runserver
```

Server is avilable on:

```
http://127.0.0.1:8000/stats/
```
## Running in Docker

Qwizi create docker-compose to this server

For build container enter in main location:
```
docker-compose up --build
```
Server is avilable on:

```
http://localhost:3000/
```
