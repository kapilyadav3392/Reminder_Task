from rest_framework.views import APIView
from .models import Reminder
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer

class ReminderListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            reminders = Reminder.objects.all()
          
            if not reminders:
                context = {
                    "status": status.HTTP_404_NOT_FOUND,
                    "sucess": True,
                    "message": "Data does not exist"
                    
                }
                
                return Response(context,status=status.HTTP_404_NOT_FOUND)

            else:
               
                serializer = ReminderSerializer(reminders, many=True)
                context = {
                    "status": status.HTTP_200_OK,
                    "sucess": True,
                    "data": serializer.data
                    
                }
                return Response(context,status=status.HTTP_200_OK)
                
                
        except Exception as error:
            context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "sucess": False,
                    "error": str(error)
                    
                }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
        
            serializer = ReminderSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                
                context = {
                    "status": status.HTTP_201_CREATED,
                    "sucess": True,
                    "data": serializer.data,
                    "message": "seccefully created"
                    
                }
                return Response(context, status=status.HTTP_201_CREATED)
        except Exception as error:
            context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "sucess": False,
                    "error": str(error)
                    
                }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            reminder = Reminder.objects.get(pk=pk)
            serializer = ReminderSerializer(reminder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                context = {
                    "status": status.HTTP_200_OK,
                    "sucess": True,
                    "message": "succefully updates",
                    "data": serializer.data
                    
                }
                return Response(context,status=status.HTTP_200_OK)
        except Exception as error:
            context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "sucess": False,
                    "error": str(error)
                    
                }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            reminder = Reminder.objects.get(pk=pk)
            reminder.delete()
            context = {
                    "status": status.HTTP_200_OK,
                    "sucess": True,
                    "message": "succefully deleted",
                    
                    
                }
            return Response(context,status=status.HTTP_200_OK)
            
        except Exception as error:
            context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "sucess": False,
                    "error": str(error)
                    
                }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
    
class ReminderDetailAPIView(APIView):
    def get(self, request,pk , *args, **kwargs):
        try:
            reminder = Reminder.objects.get(pk=pk)
            serializer = ReminderSerializer(reminder)
            context = {
                    "status": status.HTTP_200_OK,
                    "sucess": True,
                    "data": serializer.data,
                    
                    
                }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as error:
            context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "sucess": False,
                    "error": str(error)
                    
                }
            
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        