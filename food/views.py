from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class FoodViewset(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer