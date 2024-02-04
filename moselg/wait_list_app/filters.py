import django_filters
from django.forms import DateInput
from django_filters import DateFilter, CharFilter
from django_filters.widgets import RangeWidget


from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(label='Дата начала отбора', field_name='create_at', lookup_expr='gte')
    end_date = DateFilter(label='Дата заверш/. отбора', field_name='create_at', lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = ReportBeds
        fields = '__all__'
        # exclude = ['f_employ', 'm_employ', 'f_free', 'm_free', 'create_at'] # - исключаем поля для фильтрации

class FilterZayavki(django_filters.FilterSet):
    start_date = DateFilter(label='Дата начала отбора', field_name='create_at', lookup_expr='gte')
    # end_date = DateFilter(label='Дата заверш. отбора', field_name='create_at', lookup_expr='lte')
    end_date1 = DateFilter(label='Дата зав. отбора',
                           field_name='create_at',
                           lookup_expr='lte',
                           widget=DateInput(attrs={'type': 'date'})
                           )

    class Meta:
        model = ZayavkaNaGospit
        fields = '__all__'
        # exclude = ['f_employ', 'm_employ', 'f_free', 'm_free', 'create_at'] # - исключаем поля для фильтрации

class FilterKis(django_filters.FilterSet):
    start_date = DateFilter(label='Дата начала отбора',
                            field_name='date_out',
                            lookup_expr='gte',
                            widget=DateInput(attrs={'type': 'date'}))
    # end_date = DateFilter(label='Дата заверш. отбора', field_name='create_at', lookup_expr='lte')
    end_date1 = DateFilter(label='Дата зав. отбора',
                           field_name='date_out',
                           lookup_expr='lte',
                           widget=DateInput(attrs={'type': 'date'})
                           )

    class Meta:
        model = Kis
        # fields = '__all__'
        fields = []
        # exclude = ['fio', 'date_gospit', 'date_out' ] # - исключаем поля для фильтрации
