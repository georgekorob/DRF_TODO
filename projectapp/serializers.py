from rest_framework.serializers import HyperlinkedModelSerializer
from projectapp.models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
