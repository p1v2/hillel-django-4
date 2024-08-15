from django.db import models
from products.models import Product


class Store(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	products = models.ManyToManyField(Product, through='inventory.Inventory', related_name='stores')

	def __str__(self):
		return self.name
