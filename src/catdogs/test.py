from django.test import TestCase
from django.urls import reverse


class CD_test(TestCase):

    def test_get(self):
        request = self.client.get(reverse('CD'))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, template_name='choice.html')
