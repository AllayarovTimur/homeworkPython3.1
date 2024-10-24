from msilib.schema import ListView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from eployees_app.models import Employees


# Create your views here.

class EmployeesList(ListView):
    template_name = 'employees/employees_list.html'
    model = Employees
    context_object_name = 'employees'

class EmployeeDetail(DetailView):
    template_name = 'employees/employee_detail.html'
    model = Employees
    context_object_name = 'employee'

class EmployeeUpdate(UpdateView):
    template_name = 'employees/employee_edit.html'
    model = Employees
    context_object_name = 'employee'
    fields = ['employeeSurname',
              'employeeName',
              'employeePatronymic',
              'employeeJobTitle',
              'employeeBirthDate',
              'employeePhoto'
              ]
    def get_success_url(self):
        return reverse_lazy('employee_detail', kwargs={'pk': self.object.pk} )

class EmployeeCreate(CreateView):
    template_name = 'employees/employee_create.html'
    model = Employees
    context_object_name = 'employee'
    fields = ['employeeSurname',
              'employeeName',
              'employeePatronymic',
              'employeeJobTitle',
              'employeeBirthDate',
              'employeePhoto'
              ]

    def get_success_url(self):
        return reverse_lazy('employee_detail', kwargs={'pk': self.object.pk})

class EmployeeDelete(DeleteView):
    template_name = 'employees/employee_confirm_delete.html'
    model = Employees
    context_object_name = 'employee'
    success_url = reverse_lazy('employees_list')