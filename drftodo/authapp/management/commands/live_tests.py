import os
from django.core.management import BaseCommand
from requests.auth import HTTPBasicAuth
from rest_framework.test import CoreAPIClient
from projectapp.models import Todo


class Command(BaseCommand):
    name = os.getenv('SUPER_USER_USERNAME')
    password = os.getenv('SUPER_USER_PASSWORD')
    url = 'http://127.0.0.1:8000/api/todos/'

    def handle(self, *args, **options):
        self.live_test_get_todo()

    def live_test_get_todo(self):
        count_of_object = Todo.objects.count()
        client = CoreAPIClient()
        client.session.auth = HTTPBasicAuth(self.name, self.password)
        schema = client.get(self.url)
        assert(len(schema) == count_of_object)
