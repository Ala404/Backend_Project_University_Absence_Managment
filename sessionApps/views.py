
from rest_framework import status
from rest_framework.response import Response
from .models import Session
from .serializers import SessionsSerializer
from rest_framework.decorators import api_view
# Create your views here.

date_json =  {
        "sess_date": ""
    }

@api_view(['GET', 'POST'])
def session_list(request):
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionsSerializer(sessions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # if request.data['sess_date'] :
        #     date_json['sess_date'] = request.data['sess_date']
        #     date_serializer = SessionDatesSerializer(data=date_json)
        #     if date_serializer.is_valid():
        #         date_serializer.save()
        #         request.data['date'] = date_serializer.data['id_date']
        #         request.data.pop('sess_date')
        #     else:
        #         return Response(date_serializer.errors, status=400)
            
            
        serializer = SessionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def session_detail(request, pk):
    try:
        session = Session.objects.get(pk=pk)
        # date = SessionDate.objects.get(pk=session.date.id_date)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionsSerializer(session)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        # if request.data['sess_date'] :
        #     date_json['sess_date'] = request.data['sess_date']
        #     date_serializer = SessionDatesSerializer(date,data=date_json)
        #     if date_serializer.is_valid():
        #         date_serializer.save()
        #         request.data['date'] = date_serializer.data['id_date']
        #         request.data.pop('sess_date')
        #     else:
        #         return Response(date_serializer.errors, status=400)
        
        serializer = SessionsSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#/////////////////sessionDates////////////////////
# @api_view(['GET', 'POST'])
# def datasession_list(request):
#     if request.method == 'GET':
#         sessions = SessionDate.objects.all()
#         serializer = SessionDatesSerializer(sessions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SessionDatesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def datasession_detail(request, pk):
    # try:
    #     session = SessionDate.objects.get(pk=pk)
    # except SessionDate.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = SessionDatesSerializer(session)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = SessionDatesSerializer(session, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     session.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)