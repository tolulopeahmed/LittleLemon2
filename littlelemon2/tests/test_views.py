# test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Item1", price=50)
        Menu.objects.create(title="Item2", price=60)

    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        menu_items = Menu.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), menu_items.count())
