![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
# Hi there, I'm [Timofey - Razborshchikov](https://github.com/Timofey3085) ![](https://github.com/blackcater/blackcater/raw/main/images/Hi.gif) 
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
