from django.contrib import admin
from eployees_app import models
# Register your models here.
@admin.register(models.Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['employeeSurname', 'employeeName', 'employeePatronymic', 'employeeJobTitle', 'employeeBirthDate', 'employeePhoto']

@admin.register(models.Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['departmentName', 'departmentBoss', 'departmentEmployeesCount']

@admin.register(models.Accounting)
class AccountingAdmin(admin.ModelAdmin):
    list_display = ['employeeName', 'employeeSalary']

@admin.register(models.WorkPlan)
class WorkPlanAdmin(admin.ModelAdmin):
    list_display = ['task', 'dateCreation', 'deadline', 'customerOrganization', 'taskDescription']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerName']