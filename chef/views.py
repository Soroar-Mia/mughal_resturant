from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ChefViewset(viewsets.ModelViewSet):
    queryset = models.Chef.objects.all()
    serializer_class = serializers.ChefSerializer