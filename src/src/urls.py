"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_01.views import *
from django_02.views import tp
from django_03.views import *
from django_04.views import login
from test_00.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('two_pow/<int:number>', tp, name='dt'),
    path('word/<iword>', word, name='word'),
    path('word2/<iword>', word2, name='word2'),
    path('login', login, name='login'),
    path('django_09_end/', include('django_09_end.urls')),
]
