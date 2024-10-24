from django.template.defaultfilters import length
from rest_framework import serializers
from eployees_app import models

class Employees(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = '__all__'

class WorkPlan(serializers.ModelSerializer):
    employeeId = Employees(read_only=True)
    employeeId_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()
    class Meta:
        model = models.WorkPlan
        fields = '__all__'

    def get_price(self, obj):
        if models.WorkPlan.objects.filter(task=obj).exists():
            return len(obj.task)*50