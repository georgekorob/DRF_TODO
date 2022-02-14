from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from projectapp.models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


# Create your views here.
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
