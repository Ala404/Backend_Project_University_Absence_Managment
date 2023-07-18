from rest_framework import serializers
from .models import Session



class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


# class SessionDatesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SessionDate
#         fields = '__all__'