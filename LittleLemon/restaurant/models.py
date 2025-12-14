from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Booking(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(11)])
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateTimeField()

class Menu(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(5)])
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)