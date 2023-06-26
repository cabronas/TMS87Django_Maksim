import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
1

# Create your views here.
def word(request, iword):
    if len(iword) % 2 == 0:
        return redirect('admin:index')
    else:
        return redirect('word2', iword)


# return HttpResponse(f'{2 ** number}')

def word2(request, iword):
    return HttpResponse(f'{iword[::2]}')
