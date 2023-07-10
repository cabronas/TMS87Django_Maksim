from django.contrib import admin
from django.urls import path, include

from school.views import *

urlpatterns = [
    path('groups', show_gr, name='show_gr'),
    path('std_of_gr/<int:grid>', stud_of_gr, name='stud_of_gr'),
]