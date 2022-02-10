from rest_framework.serializers import HyperlinkedModelSerializer
from authapp.serializers import UserModelSerializer
from projectapp.models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    project = ProjectModelSerializer()
    user = UserModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
