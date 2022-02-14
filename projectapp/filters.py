from django_filters import rest_framework as filters
from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    first_date = filters.DateFilter(field_name="create_date", lookup_expr='gte')
    last_date = filters.DateFilter(field_name="create_date", lookup_expr='lte')

    class Meta:
        model = Todo
        fields = ['project']
