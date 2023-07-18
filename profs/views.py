from profiles.models import Profile
from django.shortcuts import render
from django.http import HttpResponse

from profiles.serializers import ProfileSerializer
from .models import Prof
from .serializers import ProfSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.



@api_view(['GET', 'POST'])
def prof_list (request):
    if request.method == 'GET':
        profs = Prof.objects.all()
        serializer = ProfSerializer(profs, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        
        prof_profile_json = { 
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "prof"
                        }
        data_keys = list(request.data.keys())
        for i in data_keys :
            print(i)
            for j in prof_profile_json.keys():
                if i == j:
                    prof_profile_json[j] = request.data[i]
                    request.data.pop(i)
                    
        profile_serializer = ProfileSerializer(data=prof_profile_json)
        if profile_serializer.is_valid():
            profile_serializer.save()
            request.data['profile'] = profile_serializer.data['id_profile']
        
        
        
        serializer = ProfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def prof_detail(request, pk):
    try:
        prof = Prof.objects.get(pk=pk)
    except Prof.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProfSerializer(prof)
        return Response(serializer.data)
    elif request.method == 'PUT':
        profile_id = prof.profile.id_profile
        proflie_id_to_str = str(profile_id)
        prof_profile_json = { 
                        "id_profile": proflie_id_to_str,
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "prof"
                        }

        profilee = Profile.objects.get(pk=profile_id)
        data_keys = list(request.data.keys())

        for i in data_keys :
           
            for j in prof_profile_json.keys():
                if i == j:
                    prof_profile_json[j] = request.data[i]
                    print(j)
                    request.data.pop(i)


        serializer = ProfSerializer(prof, data=request.data)
        if serializer.is_valid():
            serializer.save()


            profile_serializer = ProfileSerializer(profilee, data= prof_profile_json)
            profile_serializer.is_valid()
            print(profile_serializer)
            try:
                
                profile_serializer.save()

                updated_data = profile_serializer.data | serializer.data
                return Response(updated_data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e))
       
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prof.delete()
        return Response(status=204)


