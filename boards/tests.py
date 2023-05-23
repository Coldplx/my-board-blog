from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home
from .models import Board

# Create your tests here.
def create_instances_model():
    Board.objects.create(name='Django', description='Django discussion board.')
    Board.objects.create(name='Python', description='General discussion about Python.')
    Board.objects.create(name='Random', description='Here you can discuss about anything')


# class HomeTests(TestCase):

#     def test_home_view_status(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_home_url_resolve_home_view(self):
#         view = resolve('/')
#         self.assertEqual(view.func, home)

