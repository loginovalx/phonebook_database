# Phonebook

Консольное приложение телефонной книги на Python с хранением данных в PostgreSQL.

## Что умеет

- показать все контакты;
- добавить контакт;
- обновить контакт по `id`;
- удалить контакт по `id`;
- найти контакт по `id`.

## Стек

- Python 3.11
- PostgreSQL 16
- pgAdmin 4
- Docker Compose

## Структура проекта

```text
.
├── app
│   ├── db.py
│   └── main.py
├── sql
│   └── init.sql
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Запуск

### 1. Поднять базу данных и pgAdmin

```bash
docker compose up -d db pgadmin
```

Сервисы будут доступны по адресам:

- PostgreSQL: `localhost:5432`
- pgAdmin: `http://localhost:5050`

Данные для входа:

- PostgreSQL database: `phonebook`
- PostgreSQL user: `user`
- PostgreSQL password: `qwert1234`
- pgAdmin email: `noemail@mail.user`
- pgAdmin password: `qwert1234`

### 2. Запустить приложение

Для интерактивной работы удобнее запускать приложение отдельной командой:

```bash
docker compose run --rm app
```

Если образ еще не собран, Compose соберет его автоматически.

## Меню приложения

После запуска доступны действия:

```text
1. Show contacts
2. Add contact
3. Update contact
4. Delete contact
5. Find by id
6. Exit
```

## Валидация данных

- `first_name` и `last_name` должны быть не длиннее 20 символов;
- `phone` должен содержать от 10 до 15 цифр и может начинаться с `+`.

## Инициализация базы

При первом запуске PostgreSQL автоматически выполняется файл `sql/init.sql`, который создает таблицу `contacts`.

Структура таблицы:

- `id` - `SERIAL PRIMARY KEY`
- `first_name` - `VARCHAR(20)`
- `last_name` - `VARCHAR(20)`
- `phone` - `VARCHAR(20)`
- `note` - `TEXT`

## Полезные команды

Остановить контейнеры:

```bash
docker compose down
```

Остановить контейнеры и удалить том с данными:

```bash
docker compose down -v
```

Пересобрать приложение:

```bash
docker compose build app
```

## Примечание

Приложение подключается к базе по имени хоста `db`, поэтому его нужно запускать внутри Docker Compose, а не напрямую локальной командой `python`.
