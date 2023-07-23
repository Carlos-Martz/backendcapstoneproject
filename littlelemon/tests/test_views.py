from django.test import TestCase, RequestFactory
from restaurant import views, models, serializers


class MenuViewTest(TestCase):
  def setUp(self):
    models.Menu.objects.create(title="pizza", price=11, inventory=15)
    models.Menu.objects.create(title="coffee", price=1.50, inventory=85)
  
  def test_getall(self):
    menu = models.Menu.objects.all()
    result = []
    for item in menu:
      result.append(str(item))
    expected_result = ["pizza: 11.00", "coffee: 1.50"]
    self.assertEqual(result, expected_result)
