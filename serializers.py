from rest_framework import serializers
from .models import Apartments, User

class showApartmentDetails(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'

