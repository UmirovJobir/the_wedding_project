
from rest_framework import serializers
from services.models.restoran import  RestoranModel, BookedDate, EvantModel, TableModel


class BookedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedDate
        fields = ('date',)

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = ('id', 'name', 'type', 'price')

class RestoranSerializer(serializers.ModelSerializer):
    booked_dates = BookedDateSerializer(many=True)

    class Meta:
        model = RestoranModel
        fields = ('id', 'event_id', 'restoran', 'city', 'address', 'image', 'booked_dates')


class EvantSerializer(serializers.ModelSerializer):

    class Meta:
        model = EvantModel
        fields = ('id', 'image', 'name', 'active')
