from rest_framework import serializers
from . import models

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chef
        fields = '__all__'