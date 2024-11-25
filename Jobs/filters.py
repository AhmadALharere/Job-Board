import django_filters
from .models import Jobs


class jobFelter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    vacancy = django_filters.NumberFilter(field_name='vacancy',lookup_expr='gte')
    salary = django_filters.NumberFilter(field_name='salary',lookup_expr='gte')
    qualification = django_filters.NumberFilter(field_name='qualification',lookup_expr='lte')
    class Meta:
        model = Jobs
        fields=['title','description','job_Type','vacancy','salary','category','qualification']
