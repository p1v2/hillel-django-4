from orders.models import Order, OrderProduct
from rest_framework import serializers

from products.serializers import ProductSerializer


class OrderProductViewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')

    def to_representation(self, instance):
        return OrderProductViewSerializer().to_representation(instance)


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('uuid', 'user', 'order_products', 'created_at')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        order_products = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)

        for order_product in order_products:
            OrderProduct.objects.create(order=order, **order_product)

        return order
