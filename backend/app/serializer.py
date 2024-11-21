from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React  # Removed the comma
        fields = ['employee', 'department']
