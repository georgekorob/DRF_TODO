from rest_framework.viewsets import ModelViewSet
from projectapp.models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
