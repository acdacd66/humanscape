from rest_framework import serializers
from .models import  ClinicalData

class ClinicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalData
        fields = '__all__'