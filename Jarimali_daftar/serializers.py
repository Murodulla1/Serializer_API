from rest_framework import serializers

from . models import Fines

class FinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fines
        fields = '__all__'



