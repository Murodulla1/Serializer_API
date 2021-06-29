from rest_framework import serializers

from . models import Commands_table

class Commands_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commands_table
        fields = '__all__'


