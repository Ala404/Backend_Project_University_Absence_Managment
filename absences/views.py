from django.shortcuts import render
from .models import Absence
from .serializers import AbsenceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def absence_list(request):
    if request.method == 'GET':
        data = Absence.objects.all()
        serializer = AbsenceSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AbsenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def absence_detail(request, id, format=None):
    try:
        absence = Absence.objects.get(pk=id)
    except Absence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AbsenceSerializer(absence)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AbsenceSerializer(absence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        absence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    