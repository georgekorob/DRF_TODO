from django.test import TestCase
from mixer.backend.django import mixer
from requests.auth import HTTPBasicAuth
from authapp.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient,\
    APITestCase, CoreAPIClient
from projectapp.models import Project, Todo
from projectapp.views import ProjectModelViewSet


class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.admin = User.objects.create_superuser(self.name, self.email, self.password)
        self.data = {'name': 'jessicabelt12', 'link': 'https://github.com/jessicabelt12/project0'}
        self.data_put = {'name': 'barbaramart16'}
        self.url = '/api/projects/'

    def tearDown(self) -> None:
        pass

    # APIRequestFactory
    def test_factory_get_list_admin(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        force_authenticate(request, self.admin)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        data = self.data.copy()
        data.update(users=[1])
        request = factory.post(self.url, data, format='json')
        force_authenticate(request, self.admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_client_create_admin(self):
        project = Project.objects.create(**self.data)
        project.users.add(self.admin)
        project.save()
        client = APIClient()
        client.login(username=self.name, password=self.password)
        # client.force_login(self.admin)
        response = client.patch(f'{self.url}{project.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_ = Project.objects.get(id=project.id)
        self.assertEqual(project_.name, self.data_put.get('name'))

        client.logout()


# APITestCase
class TestProject(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    def tearDown(self) -> None:
        pass

    def test_put_mixer_project(self):
        project = mixer.blend(Project, name='startname')
        self.client.login(username=self.name, password=self.password)
        response = self.client.patch(f'/api/projects/{project.id}/', {'name': 'somename'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_ = Project.objects.get(id=project.id)
        self.assertEqual(project_.name, 'somename')
        self.client.logout()

    def test_put_mixer_todo(self):
        todo = mixer.blend(Todo, text='starttext')
        self.client.login(username=self.name, password=self.password)
        response = self.client.patch(f'/api/todos/{todo.id}/', {'text': 'sometext'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo_ = Todo.objects.get(id=todo.id)
        self.assertEqual(todo_.text, 'sometext')
        self.client.logout()

    def test_core_api(self):
        count_of_test_object = 5
        mixer.cycle(count_of_test_object).blend(Todo)
        client = CoreAPIClient()
        client.session.auth = HTTPBasicAuth(self.name, self.password)
        schema = client.get('http://testserver/api/todos/')
        assert(len(schema) == count_of_test_object)
