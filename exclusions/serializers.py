from rest_framework import serializers
from .models import Exclusion

class ExclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusion
        fields = '__all__'