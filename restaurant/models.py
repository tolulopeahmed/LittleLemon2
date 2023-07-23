# models.py

from django.db import models

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    BookingDATE = models.DateField()

    def __str__(self):
        return self.name
