from rest_framework import serializers
from services.models import ServiceModel, Category, EvantModel, MenuModel
from services.serializers.restoran_serializer import EvantSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ServiceSerializer(serializers.ModelSerializer):
    category_type = serializers.PrimaryKeyRelatedField(read_only=True)
    event_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ServiceModel
        fields = ('category_type', 'name', 'type', 'price', 'image', 'file', 'description', 'event_type') 
    
    def create(self, validated_data):
        category_type_data = validated_data.pop('category_type')
        category = Category.objects.create(**validated_data)
        for category_d in category_type_data:
            Category.objects.create(category_type=category, **category_d)
        return category
    
class MenuSerializer(serializers.ModelSerializer):
    # event_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = MenuModel
        fields = ('id', 'event_id', 'name', 'type', 'price', 'image')