from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home

# Create your tests here.

class HomeTests(TestCase):

    def test_home_view_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)