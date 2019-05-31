# django_rest_project

## Установка и настройка:

Установить python версией не ниже 3.5 ==> https://www.python.org/downloads/ далее, запустить файл предварительной настройки [presetting.py](https://github.com/mikibouns/django_rest_project/blob/master/presetting.py), для этого необходимо находиться в каталоге проекта (django_rest_project):
  + *Windows*  
     ```python presetting.py```
  + *Linux*  
     ```python3 presetting.py```   
     или  
     ```chmod +x presetting.py && ./presetting.py```  
  + *MacOS*  
     ```python3 presetting.py```  

### Активация виртуальной среды
Активировать виртуальную можно следующим способом, для этого необходимо находиться в каталоге проекта (django_rest_project):  
  + *Windows*  
      ```venv\Scripts\activate.bat```
      > возможно прийдется указать абсолютный путь в файлу `activate.bat`
  + *Linux*  
      ```. env/bin/activate```  
      или  
      ```source env/bin/activate```  
  + *MacOS*  
     ```. env/bin/activate```  
     или  
     ```source env/bin/activate```
> Деактивируется виртуальная среда командой `deactivate`

### Создание и настройка БД

> Следующие команды необходимо выполнить в порядке очереди в [виртуальной среде](#Активация-виртуальной-среды). 

1) `cd rest_project` - переходим в каталог проекта

2) `python manage.py fill_db` - [fill_db](https://github.com/mikibouns/django_rest_project/blob/master/rest_project/main_app/management/commands/fill_db.py) удаляет миграции и БД если они существовали, 
   создает новые миграции и БД, затем заполняет БД тестовыми данными (БД используется SQlite, с другими БД не работает)

> Команда для запуска сервера

`python manage.py runserver` - запускает локальный веб-сервер,
который доступен по адресу 127.0.0.1:8000.
Если нужно указать другой порт или сделать
адрес доступным в локальной сети то выполняем следующую команду:
python manage.py runserver 0.0.0.0:8080 - где 8080 это номер порта

После [установки и настройки](#Установка-и-настройка) проекта вам будет доступна панель администрирования http://127.0.0.1:8000/admin/ и RootAPI http://127.0.0.1:8000/api/v1/.

Учетные данные суперпользователя: 
```
login: administ
password: Testtest123
```

## Авторизация и аутентификация

Регистрация нового пользователя:

+ URL: http://127.0.0.1:8000/api/v1/users/
+ method: POST
>Request
```buildoutcfg
{
  "address": "<string>",
  "fio": "<string>",
  "password": "<string>"
}
```
>Response
```
{
    "success": 1,
    "user_id": 8,
    "token": "35edb217ece459a3175ffe4995627bef4c085b0e"
}
```

Как получить токен зарегестрированному пользователю:
+ URL: http://127.0.0.1:8000/api/v1/get_token/
+ method: POST
>Request
```buildoutcfg
{
  "username": "<string>",
  "password": "<string>"
}
```
>Response
```buildoutcfg
{
  "token": "1d7bdc13b9f7fe39355d9811f20abec461ce884d"
}
```
Аутентифицированных токеном. Например:
```
curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 35edb217ece459a3175ffe4995627bef4c085b0e'
```

