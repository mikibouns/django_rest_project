# django_rest_project

## Установка и настройка:

Установить python версией не ниже 3.4 ==> https://www.python.org/downloads/ далее, запустить файл установки виртуальной среды [install_env.py](https://github.com/mikibouns/django_rest_project/blob/master/install_env.py), для этого необходимо находиться в каталоге проекта (django_rest_project):
  + *Windows*  
     ```python install_env.py```
  + *Linux*  
     ```python3 install_env.py```   
     или  
     ```chmod +x install_env.py && ./install_env.py```  
  + *MacOS*  
     ```python3 install_env.py```  

### Активация виртуальной среды
Активировать виртуальную можно следующим способом, для этого необходимо находиться в корневом каталоге (django_rest_project):  
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

### Команды выполняемые в виртуальной среде

> Данные команды следует выполнить в порядке очереди для настройки базы данных

1) `cd rest_project` - переходим в каталог проекта

2) `python manage.py fill_db` - [fill_db](https://github.com/mikibouns/django_rest_project/blob/master/rest_project/main_app/management/commands/fill_db.py) удаляет созданные миграции и БД (доступно для SQLite), затем
   создает БД и заполняет ее тестовыми данными

> Команда для запуска сервера

1) `python manage.py runserver` - запускает локальный веб-сервер,
   который доступен по адресу 127.0.0.1:8000.
   Если нужно указать другой порт или сделать
   адрес доступным в локальной сети то выполняем следующую команду:
   python manage.py runserver 0.0.0.0:8080 - где 8080 это номер порта

После [установки и настройки](#Установка-и-настройка) проекта вам будет доступна панель администрирования по адресу http://127.0.0.1:8000/admin/ и RootAPI по адресу http://127.0.0.1:8000/api/v1/.

Учетные данные суперпользователя следующие: 
```
login: administ
password: Testtest123
```
