import django_filters
from .models import Test, UserTest


class TestFilter(django_filters.FilterSet):
    min_worktime = django_filters.NumberFilter(field_name='WorkTime', lookup_expr='gte')
    max_worktime = django_filters.NumberFilter(field_name='WorkTime', lookup_expr='lte')

    class Meta:
        model = Test
        fields = ['min_worktime', 'max_worktime']

class UserTestSearch(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='UserName', lookup_expr='icontains')

    class Meta:
        model = UserTest
        fields = ['username']