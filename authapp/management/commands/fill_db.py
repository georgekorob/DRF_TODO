import json
import os
import random
import names
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from authapp.models import User
from projectapp.models import Project, Todo
from mixer.backend.django import mixer


def load_from_json(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as infile:
            return json.load(infile)
    except UnicodeDecodeError:
        with open(file_name, mode='r', encoding='windows-1251') as infile:
            return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        if os.path.exists('db.sqlite3'):
            os.remove('db.sqlite3')
        print('deleted db.sqlite3')
        for dirapp in os.listdir():
            if os.path.isdir(dirapp) and os.path.exists(f'{dirapp}/migrations'):
                for filemig in os.listdir(f'{dirapp}/migrations'):
                    if filemig not in ['__init__.py', '__pycache__']:
                        filename = f'{dirapp}/migrations/{filemig}'
                        os.remove(filename)
                        print(f'deleted {filename}')
        print('makemigrations...')
        call_command('makemigrations')
        print('migrate...')
        call_command('migrate')
        User.objects.create_superuser(username=os.getenv('SUPER_USER_USERNAME'),
                                      password=os.getenv('SUPER_USER_PASSWORD'),
                                      email=os.getenv('SUPER_USER_EMAIL'))
        for i in range(40):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            username = f'{first_name}{last_name[:4]}{i}'.lower()
            User.objects.create_user(username=username,
                                     password=f'testpass',
                                     email=f'{username}@testmail.ru',
                                     first_name=first_name,
                                     last_name=last_name)
        for p_i in range(20):
            users = list(User.objects.all())
            random_users = random.sample(users, 5)
            firstusername = random_users[0].username
            project = Project.objects.create(name=f'{firstusername} project{p_i}',
                                             link=f'https://github.com/{firstusername}/project{p_i}')
            project.users.set(random_users)
            for i in range(random.randint(1, 6)):
                text = lorem_ipsum.words(random.randint(10, 20)).split()
                random.shuffle(text)
                Todo.objects.create(project=project,
                                    text=' '.join(text).capitalize(),
                                    user=random.choice(random_users) if i else users[0])

        # User.objects.all().delete()
        # for name in ['authapp']:
        #     filename = f'./{name}/fixtures/{name}.json'
        #     call_command('loaddata', filename, app_label=name)
