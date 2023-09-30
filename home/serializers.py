from rest_framework import serializers
from .models import *

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        exclude = ['film_id']

class RentalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rental