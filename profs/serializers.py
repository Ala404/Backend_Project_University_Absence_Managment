from rest_framework import serializers
from .models import Prof



class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = '__all__'
