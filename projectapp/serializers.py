from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authapp.serializers import UserModelSerializer
from projectapp.models import Project, Todo


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    # project = ProjectModelSerializer()
    # user = UserModelSerializer()

    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = ('is_active',)
