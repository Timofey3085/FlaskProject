![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
# Тестовое задание: Разработка приложения "ToDo List (Список задач)"

### Цель: Создать небольшое веб-приложение на Flask, которое предоставляет RESTful API для управления списком задач (TODO list).

#### Основные возможности:
1. Создание задачи:
- Метод: POST
- URL: /tasks/list
- Параметры запроса: объект с полями title (строка) и description (строка, опционально).
- Ответ: объект с полями id, title, description, created_at, updated_at.
2. Получение списка задач:
- Метод: GET
- URL: /tasks/list
- Ответ: список задач, где каждая задача представляет собой объект с полями id, title, description, created_at, updated_at.
3. Получение информации о задаче:
- Метод: GET
- URL: /tasks/info/id
- Ответ: объект с полями id, title, description, created_at, updated_at.
4. Обновление задачи:
- Метод: POST
- URL: /tasks/update/id
- Параметры запроса: объект с полями title (строка, опционально) и description (строка, опционально).
- Ответ: объект с полями id, title, description, created_at, updated_at.
5. Удаление задачи:
- Метод: POST
- URL: /tasks/delete/id
- Ответ: Перенаправление на страницу списка задач.

#####  В проекте выполнена валидация данных, есть реализация Pytest, код структурирован и сопровождается комментариями.

##### Способ установки:

##### Клонировать репозиторий
``` bash
git clone <https or SSH URL>
 ```
##### Перейти в папку поекта командой 
``` bash
 cd <путь>
```
##### Установить зависимости из файла 
``` bash 
pip install -r requirements.txt
```
##### Для запуска использовать терминал
```
Пример запуска сервера разработки: python app.py
```

##### Технологии: Python 3.11, Flask, HTML, CSS, SQLAlchemy, CSRF

##### Автор: [Timofey - Razborshchikov](https://github.com/Timofey3085)
