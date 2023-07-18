from django.shortcuts import render
from .models import Exclusion
from .serializers import ExclusionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def exclusion_list(request):
    if request.method == 'GET':
        data = Exclusion.objects.all()
        serializer = ExclusionSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ExclusionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def exclusion_detail(request, id, format=None):
    try:
        exclusion = Exclusion.objects.get(pk=id)
    except Exclusion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExclusionSerializer(exclusion)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ExclusionSerializer(exclusion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        exclusion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)