from django.test import TestCase
from django.urls import reverse


class ProjectTests(TestCase):
    def test_project_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(reverse('home'), '/')
