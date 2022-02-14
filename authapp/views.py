from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserModelSerializer


# Create your views here.
class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
