from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .filters import ProjectFilter
from .serializers import ProjectModelSerializer, TodoModelSerializer


# Create your views here.
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.filter(is_active=True)
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['project']

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
