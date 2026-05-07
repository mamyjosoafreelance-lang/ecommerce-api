from rest_framework import serializers
from .models import OrderItem
from django.db.models import F, Sum


class OrderItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    price = serializers.DecimalField(source="product.price", decimal_places=2, max_digits=20)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'name', 'price', 'quantity', 'date', 'total_price']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity



