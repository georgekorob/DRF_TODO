from django.test import TestCase
from authapp.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from projectapp.models import Project
from projectapp.views import ProjectModelViewSet


class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.admin = User.objects.create_superuser(self.name, self.email, self.password)
        self.data = {'name': 'jessicabelt12', 'link': 'https://github.com/jessicabelt12/project0'}
        self.data_put = {'name': 'barbaramart16', 'link': '"https://github.com/jessicabelt12/project0'}
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
