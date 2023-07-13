import requests
from django.shortcuts import render


# Create your views here.
def CD(request):
    if request.method == "GET":
        return render(request, 'choice.html')
    else:
        con = {}
        if 'cats' in request.POST:
            pic = requests.get('https://api.thecatapi.com/v1/images/search/').json()
            con = {'url': pic[0]["url"]}
        elif "dogs" in request.POST:
            pic = requests.get('https://dog.ceo/api/breeds/image/random').json()
            con = {'url': pic["message"]}
        return render(request, 'pet.html', context=con)
