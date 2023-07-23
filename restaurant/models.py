# models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    BookingDATE = models.DateField()

    def __str__(self):
        return self.name
