from django.contrib import admin
from django.urls import path, include

from catdogs.views import CD, cdSave, spam, spam_sent
from school.views import *

urlpatterns = [
    path('', CD, name='CD'),
    path('cdsave', cdSave, name='cdSave'),
    path('spam', spam, name="spam"),
    path('spam_sent', spam_sent, name="spam_sent")
]
