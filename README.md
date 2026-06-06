# Лабораторная работа 7 (Docker)

Условия работы: https://github.com/tp-lessons/lab_docker

## Описание

В проекте находится Flask-приложение, которое отображает список задач из MySQL
и позволяет добавить новую задачу через форму. Приложение запускается в
контейнере, а база данных поднимается отдельным сервисом через Docker Compose.

## Структура

```text
.
├── Dockerfile
├── app
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── templates
│       └── index.html
├── db
│   └── init.sql
└── docker-compose.yml
```

## Запуск Docker

```sh
docker build -t lab-docker .
docker run -d --name lab_docker_test -p 5000:5000 lab-docker
docker cp README.md lab_docker_test:/home/README.md
docker exec lab_docker_test ls -l /home
docker stop lab_docker_test
docker rm lab_docker_test
```

## Запуск Docker Compose

```sh
docker compose up --build -d
docker compose ps
```

Приложение доступно по адресу: http://localhost:5000

Остановка:

```sh
docker compose down -v
```
