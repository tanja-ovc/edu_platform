# Edu Platform
## Тестовое задание для "HardQode"

### Технологии

Python 3.10.7, Django 4.2, Django REST Framework 3.14

### Локальный запуск проекта

- В подходящую вам локальную директорию клонируйте репозиторий командой

  ```git clone git@github.com:tanja-ovc/edu_platform.git```

  либо

  ```git clone https://github.com/tanja-ovc/edu_platform.git```

- Находясь в директории _/edu_platform_, установите виртуальное окружение:

  ```python -m venv venv```

  В проекте используется версия Python 3.10.7.
  
- Активируйте виртуальное окружение:

  ```source venv/bin/activate``` (для MacOS)
  
  ```source venv\Scripts\activate``` (для Windows)

- Установите зависимости:

  ```pip install -r requirements.txt```

- Перейдите в директорию _/edu_project_. Выполните миграции:

  ```python manage.py migrate```

- Создайте суперпользователя:

  ```python manage.py createsuperuser```

- Запустите сервер разработки:

  ```python manage.py runserver```

  Админка будет доступна по адресу http://127.0.0.1:8000/admin/


### Тестирование API

Для тестирования API я предлагаю воспользоваться готовой коллекцией запросов в Postman. Коллекция доступна по кнопке ниже.

Примечание: будет удобнее для этой цели импортировать копию (Import a copy) коллекции к себе в Postman, чтобы без проблем отправлять запросы на localhost.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/17781130-2f112267-bd80-4518-896b-6c9cf3ce48f4?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D17781130-2f112267-bd80-4518-896b-6c9cf3ce48f4%26entityType%3Dcollection%26workspaceId%3Dbdef9af5-e761-4e4f-9e74-cd2434a8c92b)

### Описание API

- В проекте настроена авторизация пользователей по токену. Эндпоинт для получения токена:

  ```http://127.0.0.1:8000/api-token-auth/```

  Пользователь вводит логин и пароль, в ответ получает токен, который потом указывает в хедере запроса, требующего авторизации. Формат хедера:

  <img width="517" alt="Screenshot 2023-10-06 at 03 09 09" src="https://github.com/tanja-ovc/edu_platform/assets/85249138/55baa3ff-b756-4e5f-ab84-c9814b6790da">


- Эндпоинт для получения информации обо всех уроках из всех продуктов, купленных пользователем:

  ```http://127.0.0.1:8000/api/my-lessons/```

  Требуется авторизация.

  Формат ответа:

  <img width="379" alt="Screenshot 2023-10-06 at 03 26 58" src="https://github.com/tanja-ovc/edu_platform/assets/85249138/513cfb40-25fd-4a6a-b0fc-f88e003e7fa5">



  Эндпоинт модифицируется параметром _product_ для получения информации обо всех уроках только одного конкретного продукта, купленного пользователем (указывается id продукта):

  ```http://127.0.0.1:8000/api/my-lessons/?product=1```

  Требуется авторизация.

  Формат ответа:

  <img width="374" alt="Screenshot 2023-10-06 at 03 25 21" src="https://github.com/tanja-ovc/edu_platform/assets/85249138/8de1e2e1-a38d-48b2-9d8b-67d1fb5175a8">



- Эндпоинт для получения информации обо всех продуктах на платформе:

  ```http://127.0.0.1:8000/api/products/```

  Авторизация не требуется.

  Формат ответа:

  <img width="389" alt="Screenshot 2023-10-06 at 03 30 10" src="https://github.com/tanja-ovc/edu_platform/assets/85249138/233bed03-bfc9-49b1-a9ac-2d3d5d154902">


По всем эндпоинтам (кроме получения токена) подразумевается только получение данных. Логика создания сущностей и налаживания связей между ними в коде не прописана.

Небольшое пояснение о подразумевающейся логике: когда пользователь покупает продукт и становится его владельцем, в таблицу LessonWatchData сразу добавляются все уроки из этого продукта с указанием принадлежности к продукту и к пользователю. Время просмотра видео урока изначально равно 0, дата последнего просмотра не заполняется. Таким образом в базе появляются данные обо всех купленных уроках, даже если пользователь ещё не заходил в урок.

### Автор проекта

Татьяна Овчинникова

октябрь 2023