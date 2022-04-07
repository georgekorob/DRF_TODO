from rest_framework.serializers import ModelSerializer
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


class TodoModelPostSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['text', 'user', 'project']
