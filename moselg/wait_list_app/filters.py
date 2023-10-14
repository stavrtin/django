import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='create_at', lookup_expr='gte')
    end_date = DateFilter(field_name='create_at', lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = ReportBedsMod
        fields = '__all__'
        exclude = ['f_employ', 'm_employ', 'create_at'] # - исключаем поля для фильтрации
