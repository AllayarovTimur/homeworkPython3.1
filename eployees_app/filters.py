from random import choices

import django_filters
import eployees_app.models
from django.db.models import Q

class Employees(django_filters.FilterSet):
    fio = django_filters.CharFilter(method='filter_fio', label='ФИО')
    salary_range = django_filters.RangeFilter(field_name='accounting__employeeSalary', label='Зарплата от и до')
    is_trainee = django_filters.BooleanFilter(method='filter_is_trainee', label='Стажер:')
    class Meta:
        model=eployees_app.models.Employees
        fields=['fio','employeeJobTitle','salary_range','is_trainee']

    def filter_is_trainee(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(accounting__employeeSalary__lte=20000)
        return queryset.filter(accounting__employeeSalary__gte=20000)

    def filter_fio(self, queryset, name, value):
        criteria = Q()
        for fio in value.split():
            criteria &= Q(employeeSurname__icontains=fio) | Q(employeeName__icontains=fio) |Q(employeePatronymic__icontains=fio)
        return  queryset.filter(criteria).distinct()