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
    # 1 another method
    # min_date = filters.DateTimeFilter(field_name="create", lookup_expr='gte', input_formats=['%Y-%m-%dT%H:%M'])
    # max_date = filters.DateTimeFilter(field_name="create", lookup_expr='lte', input_formats=['%Y-%m-%dT%H:%M'])
    # 2 another method
    # create = filters.DateFromToRangeFilter()

    class Meta:
        model = Todo
        # fields = ['project', 'create_date']
        fields = ['project']
