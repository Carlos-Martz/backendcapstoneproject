from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.IntegerField()
  booking_date = models.DateTimeField()
  
  def __str__(self):
    return self.name + ' on ' + str(self.booking_date) + ' for ' + str(self.no_of_guests)


class Menu(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.SmallIntegerField()
  
  def __str__(self):
    return f'{self.title}: {self.price}'