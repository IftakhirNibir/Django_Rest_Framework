from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializer import Student_Serializer
# Create your views here.

@api_view(['GET'])
def get_students(request):
    response = {'status': 200}
    student_objs =  Student.objects.all()
    serializer = Student_Serializer(student_objs, many=True)
    response['date'] = serializer.data
    return Response(response)

@api_view(['POST'])
def post_student(request):
    response = {'status': 200}
    data = request.data
    serializer = Student_Serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(response)
    
    return Response(serializer.error)

@api_view()#it accept get,put,post.. request
def home(request):
    response = {'status':200, 'message':'Hi, from rest'}
    return Response(response)

