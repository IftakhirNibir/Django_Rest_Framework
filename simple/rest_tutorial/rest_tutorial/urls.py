from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path('get_students_info/', get_students),
    path('post_student_info/', post_student),
    path('', home),
    path('admin/', admin.site.urls),
]



