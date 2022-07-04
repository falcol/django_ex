# django_ex

## Live reload

[Live reload](https://github.com/tjwalch/django-livereload-server)

## install poetry local

```bash
pip install poetry
```

## env

```bash
cp .env.template django_ex/.env
```

## Start development server

```bash
docker-compose up -d
```

## Add new

```bash
docker-compose exec web poetry add <package name>
docker-compose exec web poetry export -f requirements.txt --output requirements.txt
```

## Remove

```bash
docker-compose exec web poetry remove <package name>
```

## Create super User

```bash
docker-compose exec web python ./django_ex/manage.py createsuperuser
```

## migrate

```bash
docker-compose exec web python ./django_ex/manage.py makemigrations polls
docker-compose exec web python ./django_ex/manage.py migrate
```
