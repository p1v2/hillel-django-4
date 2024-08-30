from django.contrib.auth.models import User
from django.test import TestCase

from orders.models import Order, OrderProduct
from orders.serialializers import OrderSerializer
from products.models import Product


def paginated_response(order=None):
    results = []
    if order:
        results.append(OrderSerializer(order).data)

    return {
        'count': len(results),
        'next': None,
        'previous': None,
        'results': results
    }


class OrdersApiTestCase(TestCase):
    def assertEmpty(self, response):
        self.assertEqual(response.json(), paginated_response())

    def assertOrder(self, response):
        self.assertEqual(response.json(), paginated_response(self.order))

    def setUp(self):
        product = Product.objects.create(name='Coca-Cola', price=123.45)
        self.user = User.objects.create(username='vitalii')
        self.order = Order.objects.create(user=self.user)
        OrderProduct.objects.create(order=self.order, product=product, quantity=2)

    def test_no_auth(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 403)

    def test_all_ok(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertOrder(response)

    def test_different_user(self):
        self.client.force_login(User.objects.create(username='another'))
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertEmpty(response)

    def test_different_user_but_superuser(self):
        self.client.force_login(User.objects.create(username='another', is_superuser=True))
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertOrder(response)
