import json
from profiles.models import Profile
from .models import Student
from .serializers import StudentSerializer
from profiles.serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':


        stud_profile_json = { 
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "student"
                        }
        data_keys = list(request.data.keys())
        for i in data_keys :

            for j in stud_profile_json.keys():
                if i == j:
                    stud_profile_json[j] = request.data[i]
                    request.data.pop(i) 
        profile_serializer = ProfileSerializer(data=stud_profile_json)
        if profile_serializer.is_valid():
            profile_serializer.save()
            request.data['profile'] = profile_serializer.data['id_profile']

        
            
                    
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id, format=None):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        profile_id = student.profile.id_profile
        proflie_id_to_str = str(profile_id)
        stud_profile_json = { 
                        "id_profile": proflie_id_to_str,
                        "user_name": "",
                        "email": "",
                        "password": "",
                        "profile_type": "student"
                        }

        profilee = Profile.objects.get(pk=profile_id)
        data_keys = list(request.data.keys())

        for i in data_keys :
           
            for j in stud_profile_json.keys():
                if i == j:
                    stud_profile_json[j] = request.data[i]
                    print(j)
                    request.data.pop(i)


        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()


            profile_serializer = ProfileSerializer(profilee, data= stud_profile_json)
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
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)