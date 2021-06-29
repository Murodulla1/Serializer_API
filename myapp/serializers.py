from rest_framework import serializers

from . models import Employees,Ragbat

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class RagbatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ragbat
        fields = "__all__"