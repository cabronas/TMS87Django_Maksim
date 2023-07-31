from importlib import import_module

from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class CD_test(TestCase):

    def test_cd_get(self):
        request = self.client.get(reverse('CD'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='choice.html')

    def test_cd_post(self):
        request = self.client.post(reverse('CD'), {'cats': 'true'})
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='pet.html')
        request = self.client.post(reverse('CD'), {'dogs': 'true'})
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='pet.html')

    def test_mail(self):
        session = self.client.session
        session["data_for_session"] = {"url": "https://cdn2.thecatapi.com/images/imz2EwFWv.jpg",
                                       "kind": "cat",
                                       "type": "jpg"}
        session["mail"] = "cabronian123@gmail.com"
        session.save()
        request = self.client.post(reverse('spam_sent'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='spam_sent.html')

    def test_save(self):
        session = self.client.session
        session["data_for_session"] = {"url": "https://cdn2.thecatapi.com/images/imz2EwFWv.jpg",
                                       "kind": "cat",
                                       "type": "jpg"}
        session.save()
        request = self.client.post(reverse('cdSave'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='saved.html')
