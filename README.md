# Yatube – социальная сеть для публикации дневников.

## Стек:
Python 3, Django 2.2 LST, PostgreSQL, pytest, unittest.

## Описание:
Реализован пользовательский функционал:
*	Создание, редактирование и удаление постов.
*	Пагинация постов и кэширование.
*	Регистрация с верификацией данных, сменой и восстановлением пароля.
*	Профиль пользователя с возможностью редактирования личных данных.
*	Личные сообщения.
*	Возможность подиски и отписки на авторов.
*	Поиск по сайту.
*	Возможность комментировать посты.

Сайт выложен в сеть и доступен по адресу http://stroymart.pythonanywhere.com/

## Установка:
Клонируем репозиторий на локальную машину:
```$ git clone https://github.com/wiky-avis/Yatube.git```

Создаем виртуальное окружение:
```$ python -m venv venv```

Устанавливаем зависимости:
```$ pip install -r requirements.txt```

Создание и применение миграций:
```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Создаем суперпользователя:
```$ python manage.py createsuperuser --email admin@admin.com --username admin```

Запускаем django сервер:
```$ python manage.py runserver```

## Примеры запросов к API:
Для формирования ответов и запросов будет использовано расширение для VS Code [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

Расширение REST Client позволяет прямо из VS Code отправлять HTTP-запросы, и в этом же интерфейсе просматривать ответы на них. Установка расширения стандартна: в строке поиска панели "Extensions" нужно ввести название плагина "REST Client" и нажать кнопку "Install" («Установить»).

Запросы в REST Client нужно сохранять в файле с расширением .http. После установки создайте в VS Code новый файл (например requests.http). Запросы в файле отделяются друг от друга строками, содержащими три символа #.

Для отправки любого запроса нажмите над ним ссылку "SendRequest". В правой части экрана вы увидите ответ сервера:

![GitHub Logo](/images/окно_вскод.jpg)
