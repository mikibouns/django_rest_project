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
