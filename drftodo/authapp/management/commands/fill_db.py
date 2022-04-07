import json
import os
import platform
import random
import names
from django.contrib.auth.models import Group, Permission
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from authapp.models import User
from projectapp.models import Project, Todo


def load_from_json(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as infile:
            return json.load(infile)
    except UnicodeDecodeError:
        with open(file_name, mode='r', encoding='windows-1251') as infile:
            return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        if platform.system() == 'Windows':
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
        if User.objects.count() == 0:
            User.objects.create_superuser(username=os.getenv('SUPER_USER_USERNAME'),
                                          password=os.getenv('SUPER_USER_PASSWORD'),
                                          email=os.getenv('SUPER_USER_EMAIL'))
            users = []
            for i in range(20):
                first_name = names.get_first_name()
                last_name = names.get_last_name()
                username = f'{first_name}{last_name[:4]}{i}'.lower()
                users.append(User(username=username,
                                  password=f'geekbrains',
                                  email=f'{username}@geekbrains.ru',
                                  first_name=first_name,
                                  last_name=last_name))
                print(f'User {i} added.')
            User.objects.bulk_create(users)
            for p_i in range(10):
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
                print(f'Project {p_i} added.')

            # for HW 6
            perms = ['add', 'change', 'delete']
            for group_name, models, user_names in [('Администраторы', [User, Project, Todo], ['Админ']),
                                                   ('Разработчики', [Todo], ['Разработчик1', 'Разработчик2']),
                                                   ('Владельцы', [Project, Todo], ['Владелец1', 'Владелец2'])]:
                group = Group.objects.create(name=group_name)
                for model in models:
                    # content_type = ContentType.objects.get_for_model(model)
                    model_name = model.__name__.lower()
                    for perm in perms:
                        permission = Permission.objects.get(codename=f'{perm}_{model_name}')
                        # permission, _ = Permission.objects.get_or_create(codename=f'can_{perm}_{model_name}',
                        #                                                  name=f'Can {perm} {model_name}',
                        #                                                  content_type=content_type)
                        group.permissions.add(permission)
                for user_name in user_names:
                    user = User.objects.create_user(username=user_name,
                                                    password=f'geekbrains',
                                                    email=f'{user_name}@geekbrains.ru',
                                                    first_name='first_name',
                                                    last_name='last_name')
                    group.user_set.add(user)

        # User.objects.all().delete()
        # for name in ['authapp']:
        #     filename = f'./{name}/fixtures/{name}.json'
        #     call_command('loaddata', filename, app_label=name)
