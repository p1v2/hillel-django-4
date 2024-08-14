from django.db import models


class Store(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

	def __str__(self):
		return self.name
