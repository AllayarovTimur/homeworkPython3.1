"""
URL configuration for employees_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from eployees_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees_list/', views.EmployeesList.as_view(), name='employees_list'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name = 'employee_detail'),
    path('employee/<int:pk>/update', views.EmployeeUpdate.as_view(), name = 'employee_update'),
    path('employee_create', views.EmployeeCreate.as_view(), name = 'employee_create'),
    path('employee/<int:pk>/delete', views.EmployeeDelete.as_view(), name = 'employee_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
