from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse(name)
    else:
        name = request.GET.get('name')
        return HttpResponse(name)
