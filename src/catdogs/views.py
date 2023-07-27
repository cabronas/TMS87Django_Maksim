import django.forms
import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from catdogs.models import AImage
from src.settings import EMAIL_HOST_USER


# Create your views here.
def CD(request):
    if request.method == "GET":
        return render(request, 'choice.html')
    else:
        session = request.session.set_expiry(30)
        con = {}
        if 'cats' in request.POST:
            pic = requests.get('https://api.thecatapi.com/v1/images/search/').json()
            con = {'url': pic[0]["url"]}
            filetype = pic[0]["url"].split('.')[-1]
            session_data = {"url": pic[0]["url"], "kind": "cat", "type": filetype}
            # AImage.objects.create(url=pic[0]["url"], kind="cat", type=filetype)
        elif "dogs" in request.POST:
            pic = requests.get('https://dog.ceo/api/breeds/image/random').json()
            con = {'url': pic["message"]}
            filetype = pic["message"].split('.')[-1]
            session_data = {"url": pic["message"], "kind": "cat", "type": filetype}
            # AImage.objects.create(url=pic["message"], kind="cat", type=filetype)
        request.session['data_for_session'] = session_data
        return render(request, 'pet.html', context=con)


def cdSave(request):
    if request.method == "POST":
        AImage.objects.create(url=request.session['data_for_session']['url'],
                              kind=request.session['data_for_session']['kind'],
                              type=request.session['data_for_session']['type'])
        con = {'url': request.session['data_for_session']['url']}
    return render(request, 'saved.html', context=con)


def spam(request):
    return render(request, 'spam.html')


def spam_sent(request):
    request.session['mail'] = request.POST.get('mail')
    send_mail(request.session['data_for_session']['kind'], request.session['data_for_session']['url'], EMAIL_HOST_USER,
              [request.session['mail']])
    return render(request, 'spam_sent.html')
# tocyxkrwugnqppix
