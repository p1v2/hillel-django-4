from django.db import models
from products.models import Product


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    store_number = models.CharField(max_length=255, null=True)
    start_time_working = models.TimeField(blank=True, null=True)
    end_time_working = models.TimeField(blank=True, null=True)
    products = models.ManyToManyField(Product, through='Inventory')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='inventory')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.PositiveIntegerField()
