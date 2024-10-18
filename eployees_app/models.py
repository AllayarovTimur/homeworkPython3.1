from django.db import models

# Create your models here.
from django.db import models

class Employees(models.Model):
    employeeSurname = models.CharField(verbose_name="Фамилия", max_length=40)
    employeeName = models.CharField(verbose_name="Имя", max_length=40)
    employeePatronymic = models.CharField(verbose_name="Отчество", max_length=40)
    jobTitleChoices = [
        ('Back-end разработчик', 'Back-end разработчик'),
        ('Front-end разработчик', 'Front-end разработчик'),
        ('Специалист отдела маркетинга', 'Специалист отдела маркетинга'),
    ]
    employeeJobTitle = models.CharField(verbose_name="Должность", max_length=30, choices=jobTitleChoices)
    employeeBirthDate = models.DateField(verbose_name="Дата рождения", auto_now=False)
    employeePhoto = models.ImageField(verbose_name="Фото", null=True)

    class Meta:
        verbose_name = 'Сотрудник',
        verbose_name_plural = 'Сотрудники',
        ordering = ['employeeSurname']

    def __str__(self):
        return f'{self.employeeSurname} {self.employeeName} {self.employeePatronymic}'


class Departments(models.Model):
    departmentName = models.CharField(verbose_name="Отдел", max_length=50, unique=True)
    bossChoices = [
        ('Генеральный директор', 'Генеральный директор'),
        ('Заместитель директора по Back-end разработке','Заместитель директора по Back-end разработке'),
        ('Заместитель директора по Front-end разработке','Заместитель директора по Front-end разработке'),
        ('Начальник отдела маркетинга','Начальник отдела маркетинга'),
    ]
    departmentBoss = models.CharField(verbose_name="Начальник", max_length=50, choices=bossChoices, default="Генеральный директор")
    departmentEmployeesCount = models.IntegerField(verbose_name="Количество сотрудников")

    class Meta:
        verbose_name = "Отдел",
        verbose_name_plural = "Отделы",
        ordering = ['departmentName']

    def __str__(self):
        return self.departmentName

class Accounting(models.Model):
    employeeName = models.OneToOneField(
        Employees,
        verbose_name="Сотрудник",
        max_length=40,
        related_name='accounting',
        on_delete=models.CASCADE,
    )
    employeeSalary = models.IntegerField(verbose_name="Зарплата")

    class Meta:
        verbose_name = 'Бухгалтерия',
        ordering = ['employeeName']

    def __str__(self):
        return f'{self.employeeName} {self.employeeSalary}'

    def getSalaryAfterTax(self):
        return 0.87*self.employeeSalary

class WorkPlan(models.Model):
    task = models.CharField(verbose_name="Задача", max_length=50)
    dateCreation = models.DateField(verbose_name="Дата создания задачи", auto_now_add=True)
    deadline = models.DateField(verbose_name="Срок сдачи", auto_now=False)
    customerOrganization = models.CharField(verbose_name="Заказчик", max_length=40)
    taskDescription = models.TextField(verbose_name="Описание задачи", blank = True,null=True)
    employeeId = models.ForeignKey(
        Employees,
        verbose_name = "Ответственный сотрудник",
        max_length = 40,
        null=True,
        on_delete = models.SET_NULL,
    )
    department = models.ForeignKey(
       Departments,
        verbose_name="Ответственный отдел",
        max_length=50,
        null= True,
        on_delete = models.CASCADE,
    )

    class Meta:
        verbose_name = 'Рабочий план',
        ordering = ['task']

    def __str__(self):
        return f'{self.task}'



class Customer(models.Model):
    customerName = models.CharField(verbose_name="Заказчик", max_length=40)
    taskId = models.ManyToManyField(
        WorkPlan,
        verbose_name="Задача",
        max_length=40,
    )

    class Meta:
        verbose_name = "Заказчик",
        verbose_name_plural = "Заказчики",
        ordering = ['customerName']

    def __str__(self):
        return self.customerName

