from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
