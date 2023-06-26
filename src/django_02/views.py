import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def tp(request, number):
    return HttpResponse(f'{2 ** number}')
