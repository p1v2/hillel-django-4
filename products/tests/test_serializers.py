from unittest.mock import patch

from django.test import TestCase

from products.models import Product, Category
from products.serializers import ProductSerializer


class SerializersTestCase(TestCase):
    def test_product_serializer(self):
        product = Product.objects.create(name='Test Product', price=100)
        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data['display_name'], 'Test Product')

    def test_product_serializer_18_plus(self):
        product = Product.objects.create(name='Test Product', price=100, is_18_plus=True)
        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data['display_name'], 'Test Product 🔞')

    def test_product_serializer_price(self):
        product = Product.objects.create(name='Test Product', price=99)
        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data['display_name'], 'Test Product 💰')

    def test_product_serializer_price_and_18_plus(self):
        category = Category.objects.create(name='Food')
        product = Product.objects.create(name='Test Product', price=99, is_18_plus=True, category=category)
        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data['display_name'], 'Test Product 🔞 💰 🍔')

    @patch('products.serializers.get_category_emoji', return_value='🔥')
    def test_product_serializer_category(self, *args):
        category = Category.objects.create(name='Food')
        product = Product.objects.create(name='Test Product', price=100, category=category)

        serializer = ProductSerializer(product)

        self.assertEqual(serializer.data['display_name'], 'Test Product 🔥')
