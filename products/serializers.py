from rest_framework import serializers

from products.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)


    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'tags')
