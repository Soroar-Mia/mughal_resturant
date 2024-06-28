from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 12)
    person = models.CharField(max_length = 12)
    date = models.DateField()
    time =models.TimeField()