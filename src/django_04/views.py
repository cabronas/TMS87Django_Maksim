from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        f = open("django_04.txt", "a")
        f.writelines([name, lname, age])
        f.close()
        return HttpResponse("Saved")
    else:
        # name = request.GET.get('name')
        return render(request, 'form.html')
