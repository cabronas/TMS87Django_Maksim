import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dt(request):
    return HttpResponse(datetime.datetime.now())
