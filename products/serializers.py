from rest_framework import serializers

from products.emojis import get_category_emoji
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

    display_name = serializers.SerializerMethodField()

    def get_display_name(self, obj: Product):
        display_name = obj.name

        if obj.is_18_plus:
            display_name += ' 🔞'

        if obj.price < 100:
            display_name += ' 💰'

        if obj.category:
            display_name += ' ' + get_category_emoji(obj.category)

        return display_name

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'tags', 'display_name')
