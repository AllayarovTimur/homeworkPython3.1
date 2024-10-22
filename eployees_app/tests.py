from django.test import TestCase
from eployees_app import factories, models
from django.urls import reverse, reverse_lazy


class EmployeesTestCase(TestCase):

    def setUp(self):
        self.employee = factories.EmployeeFactory()

    def test_get_employees_list(self):
        url = reverse('employees_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['employees'].count(), models.Employees.objects.count())

    def test_get_employee_detail(self):
        url = reverse('employee_detail', kwargs={'pk': self.employee.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_employee_update(self):
        url = reverse('employee_update', kwargs={'pk': self.employee.pk})
        old_employeeSurname = self.employee.employeeSurname

        response = self.client.post(url,
                                   {'employeeSurname': 'new_employeeSurname'},
                                   )
        self.employee.refresh_from_db()

        #self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.employee.employeeSurname, old_employeeSurname)


    def test_employee_create(self):
        url = reverse('employee_create')
        response = self.client.put(url,
                                   {'employeeSurname': 'new_employeeSurname'},
                                   {'employeeName': 'new_employeeName'},
                                   )
        self.employee.refresh_from_db()

        self.assertEqual(response.status_code, 302)
    
    def test_employee_delete(self):
        url = reverse('employee_delete', kwargs={'pk': self.employee.pk})
        old_employee_count = models.Employees.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_employee_count, models.Employees.objects.count())


