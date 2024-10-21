from rest_framework import serializers
from .models import Order
from menu.serializers import MenuItemSerializer
from customers.serializers import CustomerSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)
    customer = CustomerSerializer()
    
    class Meta:
        model = Order
        fields = '__all__'