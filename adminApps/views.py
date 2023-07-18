from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles.models import Profile

from profiles.serializers import ProfileSerializer
from .serializers import AdminSerializer
from .models import Admin
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        admin_profile_json = { 
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "admin"
                        }
        data_keys = list(request.data.keys())
        for i in data_keys :
            print(i)
            for j in admin_profile_json.keys():
                if i == j:
                    admin_profile_json[j] = request.data[i]
                    request.data.pop(i)
                    
        profile_serializer = ProfileSerializer (data=admin_profile_json)
        if profile_serializer.is_valid():
            profile_serializer.save()
            request.data['profile'] = profile_serializer.data['id_profile']
        
        
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, pk):
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin)
        return Response(serializer.data)
    elif request.method == 'PUT':
        profile_id = admin.profile.id_profile
        proflie_id_to_str = str(profile_id)
        admin_profile_json = { 
                        "id_profile": proflie_id_to_str,
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "admin"
                        }

        profilee = Profile.objects.get(pk=profile_id)
        data_keys = list(request.data.keys())

        for i in data_keys :
           
            for j in admin_profile_json.keys():
                if i == j:
                    admin_profile_json[j] = request.data[i]
                    request.data.pop(i)


        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()


            profile_serializer = ProfileSerializer(profilee, data= admin_profile_json)
            profile_serializer.is_valid()

            try:
                
                profile_serializer.save()

                updated_data = profile_serializer.data | serializer.data
                return Response(updated_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e))
    elif request.method == 'DELETE':
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)