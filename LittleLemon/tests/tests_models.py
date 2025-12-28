from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu, Booking
from django.contrib.auth.models import User

class MenuModelTest(TestCase):
    def setUp(self):
        self.menuItem = Menu.objects.create(title="IceCream", price=80)

    def test_create(self):
        self.assertEqual(self.menuItem.title, "IceCream")
        self.assertEqual(self.menuItem.price, 80)


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menuItem = Menu.objects.create(title="IceCream", price=80)
        self.user = User.objects.create_user(username='testuser', password='testpass')  

    def test_str_method(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('menu-items'))

        for item in response.data:
            menu_item = Menu.objects.get(id=item['id'])
            self.assertEqual(str(menu_item), f'{menu_item.title} : {str(menu_item.price)}')