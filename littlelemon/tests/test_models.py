from django.test import TestCase
from restaurant.models import Menu 

class MenuTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(title='chocolate cake', price=8.0, inventory=15)
    self.assertEqual(str(item), "chocolate cake: 8.0")