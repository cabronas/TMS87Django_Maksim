import time
from importlib import import_module

from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.test import override_settings

from catdogs.models import AImage


class CD_test(TestCase):

    def test_cd_get(self):
        request = self.client.get(reverse('CD'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='choice.html')

    def test_cd_post(self):
        request = self.client.post(reverse('CD'), {'cats': 'true'})
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='pet.html')
        self.assertEqual(len(self.client.session['data_for_session']['kind']), 3)
        request = self.client.post(reverse('CD'), {'dogs': 'true'})
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='pet.html')
        self.assertEqual(len(self.client.session['data_for_session']['kind']), 3)

    # @override_settings(EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend')
    def test_mail(self):
        # session = self.client.session
        # session["data_for_session"] = {"url": "https://cdn2.thecatapi.com/images/imz2EwFWv.jpg",
        #                                "kind": "cat",
        #                                "type": "jpg"}
        self.client.post(reverse('CD'), {'dogs': 'true'})
        self.client.session["mail"] = "cabronian123@gmail.com"
        request = self.client.post(reverse('spam_sent'))
        # self.assertEquals(len(mail.outbox), 1)
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='spam_sent.html')

    def test_save(self):
        self.client.post(reverse('CD'), {'cats': 'true'})
        request = self.client.post(reverse('cdSave'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='saved.html')
        self.assertEqual(AImage.objects.count(), 1)

    # def test_zero(self):
    #     self.skipTest("a")
    # with self.assertRaises(ZeroDivisionError):
    #     request = self.client.get(reverse('divide_zero_test'))
    # request = self.client.get(reverse('not_divide_zero_test'))
