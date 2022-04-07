# from rest_framework import mixins
# from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer, UserModelPropertySerializer


# Create your views here.
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserModelSerializer

    def get_serializer_class(self):
        # api/users/?version=v2
        if self.request.version == 'v2':
            return UserModelPropertySerializer
        return UserModelSerializer
