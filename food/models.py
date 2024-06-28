from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="food/images/")
    price = models.IntegerField()