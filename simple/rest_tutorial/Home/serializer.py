from rest_framework import fields, serializers
from .models import Student

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']


    
