from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

#TestCase class
class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test Menu objects
        self.item1 = Menu.objects.create(title="Pasta", price=10.99, inventory=10)
        self.item2 = Menu.objects.create(title="Pizza", price=12.99, inventory=5)
        self.item3 = Menu.objects.create(title="Salad", price=7.99, inventory=8)

    def test_getall(self):
        # Call the API endpoint
        response = self.client.get(reverse('menu-list')) 
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)