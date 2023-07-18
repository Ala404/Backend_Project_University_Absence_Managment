from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import  Schedule
from sections.models import Group
from .serializers import ScheduleSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def schedule_list(request):

    if request.method == 'GET':
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
# /////////////////////////Filter Data/////////////////////////
        schedule_filtred_tdtp = (Schedule.objects.filter(id_prof = request.data['id_prof'])
                                 |Schedule.objects.filter(classroom = request.data['classroom'])
                                 |Schedule.objects.filter(grp_num = request.data['grp_num']) 
                         )& Schedule.objects.filter(cell = request.data['cell'])
        
        is_exsist_sch  = Schedule.objects.all().filter(cell = request.data['cell'])
        is_there_cours = (Schedule.objects.filter(cell = request.data['cell']) & Schedule.objects.filter(type = 'cours')).exists()
        print(is_exsist_sch)  
        
# /////////////////////////Check if there's already a cours /////////////////////////  
     
        if is_there_cours :
            
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'you can not add a session in this cell there is a cours'})

# /////////////////////////Check if there's already a session and a inserted data is cours /////////////////////////     
        elif is_exsist_sch and request.data['type'] == 'cours' :
            
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'You can not add a cours'})
        
       
    
# /////////////////////////Check if the session TP or TD already exist and there's no cours /////////////////////////
        elif schedule_filtred_tdtp and request.data['type'] != 'cours' and not is_there_cours :
            
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Schedule already exists'})
        
        elif request.data['grp_num'] == None and request.data['type'] == 'cours' :
            request.data['grp_num'] = Group.objects.all()
        
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def schedule_detail(request, pk):

    try:
        schedule = Schedule.objects.get(pk=pk)
        sch_sess_count = Schedule.objects.filter(cell = schedule.cell).count()
    except Schedule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':

#/////////////////////////Filter Data/////////////////////////

        if sch_sess_count > 1  :
            schedule_filtred_tdtp = (Schedule.objects.filter(id_prof = request.data['id_prof'])
                                    |Schedule.objects.filter(classroom = request.data['classroom'])
                                    |Schedule.objects.filter(grp_num = request.data['grp_num']) 
                            )& Schedule.objects.filter(cell = request.data['cell'])
            
            is_exsist_sch  = Schedule.objects.all().filter(cell = request.data['cell'])
            is_there_cours = (Schedule.objects.filter(cell = request.data['cell']) & Schedule.objects.filter(type = 'cours')).exists()
            print(is_exsist_sch)  
            
    # /////////////////////////Check if there's already a cours /////////////////////////  
        
            if is_there_cours :
                
                return Response(status=status.HTTP_409_CONFLICT, data={'message': 'you can not add a session in this cell there is a cours'})

    # /////////////////////////Check if there's already a session and the updated data is cours /////////////////////////     
            elif is_exsist_sch and request.data['type'] == 'cours' :
                
                return Response(status=status.HTTP_409_CONFLICT, data={'message': 'You can not add a cours'})
        
    # /////////////////////////Check if the session TP or TD already exist and there's no cours /////////////////////////
            elif schedule_filtred_tdtp and request.data['type'] != 'cours':
                
                return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Schedule already exists'})
        
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



