from rest_framework import serializers
from . import models

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = '__all__'