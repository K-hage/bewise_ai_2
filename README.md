# Тестовое задание №2

## Стек:

- python 3.10
- Docker
- PostgreSQL 15
- FastAPI
- SQLAlchemy
- Alembic

### Запуск проекта:

- В директории с проектом создать файл .env и заполнить по образцу .env.example

- В папке с проектом в терминале прописать:

```Sh
docker-compose up --build -d
```

> Проект будет доступен по ссылке(если порт 80)
> ***[http://localhost/](http://localhost/)***

- Как остановить и очистить контейнеры:

- В папке с проектом в терминале прописать:

```Sh
docker-compose down
```

#### Описание:

Данный веб-сервис выполняет следующие функции:

1. Создание пользователя;
2. Для каждого пользователя - сохранение аудиозаписи в формате wav, преобразование её в формат mp3 и запись в базу
   данных и предоставление ссылки для скачивания аудиозаписи.

Детализация задачи:

1. Реализован веб-сервис со следующими REST методами:

- Создание пользователя, POST:

> - Принимает на вход запросы с именем пользователя;
> - Создаёт в базе данных пользователя заданным именем, так же генерирует уникальный идентификатор пользователя и UUID
    токен
    доступа (в виде строки) для данного пользователя;
> - Возвращает сгенерированные идентификатор пользователя и токен.

- Добавление аудиозаписи, POST:

> - Принимает на вход запросы, содержащие уникальный идентификатор пользователя, токен доступа и аудиозапись в формате
    wav;
> - Преобразует аудиозапись в формат mp3, генерирует для неё уникальный UUID идентификатор и сохраняет их в базе данных;
> - Возвращает URL для скачивания записи.

- Доступ к аудиозаписи, GET:

> - Предоставляет возможность скачать аудиозапись по ссылке.
