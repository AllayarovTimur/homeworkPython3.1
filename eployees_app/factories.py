import factory
from factory.django import ImageField
from eployees_app import models

class EmployeeFactory(factory.django.DjangoModelFactory):
    employeeSurname = factory.Faker('last_name')
    employeeName = factory.Faker('first_name')
    employeeBirthDate = factory.Faker('date_of_birth', minimum_age=18)
    employeePhoto = ImageField()
    class Meta:
        model = models.Employees