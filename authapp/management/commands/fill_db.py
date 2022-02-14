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
        User.objects.all().delete()
        User.objects.create_superuser(username=os.getenv('SUPER_USER_USERNAME'),
                                      password=os.getenv('SUPER_USER_PASSWORD'),
                                      email=os.getenv('SUPER_USER_EMAIL'))
        for i in range(120):
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            username = f'{first_name}{last_name[:4]}{i}'.lower()
            User.objects.create(username=username,
                                password=f'testpass',
                                email=f'{username}@testmail.ru',
                                first_name=first_name,
                                last_name=last_name)

        Project.objects.all().delete()
        Todo.objects.all().delete()
        for p_i in range(20):
            project = Project.objects.create(name=f'Проект {p_i}', link='#')
            users = list(User.objects.all())
            random_users = random.sample(users, 5)
            project.users.set(random_users)
            for i in range(3):
                Todo.objects.create(project=project,
                                    text=f'Записка {i}: {lorem_ipsum.words(10 + i)}',
                                    user=random.choice(random_users))

        # User.objects.all().delete()
        # for name in ['authapp']:
        #     filename = f'./{name}/fixtures/{name}.json'
        #     call_command('loaddata', filename, app_label=name)
