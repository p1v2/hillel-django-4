from django.db import models
from products.models import Product
from stores.models import Store

class Inventory(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()

	class Meta:
		unique_together = ('store', 'product')

	def __str__(self):
		return f"{self.quantity} of {self.product.name} at {self.store.name}"

	@property
	def total_quantity(self):
		return Inventory.objects.filter(product=self.product).aggregate(total=models.Sum('quantity'))['total']
