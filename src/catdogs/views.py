import requests
from django.shortcuts import render

from catdogs.models import AImage


# Create your views here.
def CD(request):
    if request.method == "GET":
        return render(request, 'choice.html')
    else:
        session = request.session['catdog']
        con = {}
        if 'cats' in request.POST:
            pic = requests.get('https://api.thecatapi.com/v1/images/search/').json()
            con = {'url': pic[0]["url"]}
            # filetype = pic[0]["url"].split('.')[-1]
            # AImage.objects.create(url=pic[0]["url"], kind="cat", type=filetype)
        elif "dogs" in request.POST:
            pic = requests.get('https://dog.ceo/api/breeds/image/random').json()
            con = {'url': pic["message"]}
            # filetype = pic["message"].split('.')[-1]
            # AImage.objects.create(url=pic["message"], kind="cat", type=filetype)
        return render(request, 'pet.html', context=con)


def saveCD(request):
    if request.method == "Post":
        pass
