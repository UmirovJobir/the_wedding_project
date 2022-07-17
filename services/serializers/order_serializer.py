
from rest_framework import serializers
from services.models import Order


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'restoran_id', 'table_id', 'menu_id', 'service_id', 'total_price', 'status')

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', "user_id", 'day', 'restoran_id', 'table_id', 'menu_id', 'service_id', 'total_price', 'status')
