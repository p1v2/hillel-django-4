from django.db import models

from products.models import Product


# My homework HW7


class Store(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    description = models.TextField()
    products = models.ManyToManyField(Product, through='Inventory')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('store', 'product')

    def __str__(self):
        return f"{self.product.name} at {self.store.name} - {self.quantity} in stock"
