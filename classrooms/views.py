from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Classroom
from .serializers import ClassroomSerializers
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def classroom_list(request):
    if request.method == 'GET':
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializers(classrooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        classrooms = Classroom.objects.filter(classroom_code=request.data['classroom_code'],classroom_type=request.data['classroom_type'])
        if classrooms:
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Classroom already exists'})
        serializer = ClassroomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def classroom_detail(request, pk):
    try:
        classroom = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClassroomSerializers(classroom)
        return Response(serializer.data)

    elif request.method == 'PUT':
        classroom_filtred = Classroom.objects.filter(classroom_code=request.data['classroom_code'],classroom_type=request.data['classroom_type'])
        if classroom_filtred:
            print('classroom_filtred',classroom_filtred)
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Classroom already exists'})
        serializer = ClassroomSerializers(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
