from rest_framework import serializers
from .models import Section, Group


class  SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class  GroupSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Group
        fields = '__all__'