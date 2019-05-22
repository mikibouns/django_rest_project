from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from subprocess import call
import os
import random

from product_app.models import Products


def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


try:
    for i in walklevel(os.getcwd(), level=2):
        if 'migrations' in i[0]:
            for j in i[2]:
                if j[0:2] != '__':
                    os.remove(os.path.join(i[0], j))
                    print('{} is removed'.format(j))
except:
    print('Not found!')

    call('python manage.py makemigrations', shell=True)
    call('python manage.py migrate', shell=True)


def users_iterator():
    '''генератор создание пользователей'''
    FIOs = ['Иванов Иван Иванович',
            'Петров Петр Петрович',
            'Сидоров Сергей Федорович',
            'Путин Владимир Владимирович',
            'Пушкин Александр Сергеевич',
            'Пупкин Владимир Петрович']
    for i, name in enumerate(FIOs):
        username = 'email{}@mail.com'.format(i)
        user = get_user_model()(
            fio=name,
            email=username,
            username=username,
        )
        user.set_password('123')
        yield user


def fill_products():
    '''заполнение таблицы Products'''
    roducts = ['Картофель', 'Капуста', 'Морковь', 'Помидоры', 'Огурцы', 'Чеснок', 'Лук', 'Свекла', 'Зелень', 'Яблоки']
    for prod in roducts:
        data = {'name': prod,
                'art': random.randint(123000, 999999),
                'price': random.uniform(10.50, 200.50)}
        Products.objects.create(**data)


class Command(BaseCommand):
    def handle(self, *args, **options):

        get_user_model().objects.bulk_create(iter(users_iterator())) # создание пользователей

        # Создаем суперпользователя при помощи менеджера модели
        super_user = get_user_model().objects.create_superuser('administ', 'administ@mail.com', 'Testtest123')

        fill_products() # добавляем список продуктов