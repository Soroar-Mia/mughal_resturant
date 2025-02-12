from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Customer
        fields = '__all__'