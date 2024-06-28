from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ReservationViewset(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
