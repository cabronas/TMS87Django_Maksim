from django.contrib import admin
from django.urls import path, include

from catdogs.views import CD
from school.views import *

urlpatterns = [
    path('', CD , name='CD'),
]
