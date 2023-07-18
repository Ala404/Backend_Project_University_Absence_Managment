from rest_framework import serializers
from .models import Classroom



class ClassroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'