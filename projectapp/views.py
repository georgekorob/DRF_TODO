from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Project, Todo
from .filters import ProjectFilter, TodoFilter
from .serializers import ProjectModelSerializer, TodoModelSerializer, TodoModelPostSerializer


# Create your views here.
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # Another filter
    # def get_queryset(self):
    #     queryset = Project.objects.all()
    #     name = self.request.query_params.get('name', None)
    #     if name:
    #         queryset = queryset.filter(name__contains=name)
    #     return queryset


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.filter(is_active=True)
    # pagination_class = TodoLimitOffsetPagination
    # filterset_fields = ['project']
    filterset_class = TodoFilter

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Для аутентификации с помощью JWT со стороны фронтенда, без аутентификации по сессии
            self.authentication_classes = (JWTAuthentication, )
        return super().dispatch(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TodoModelPostSerializer
        return TodoModelSerializer

    # Another method
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         instance.is_active = False
    #         instance.save()
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
