from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 99999999.99
    description = models.TextField(blank=True, null=True)
    is_18_plus = models.BooleanField(default=False)

    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='products')
    # CASCADE - delete all products in this category
    # SET_NULL - set category to NULL
    # SET_DEFAULT - set category to default value
    # RESTRICT - raise an error
    # DO_NOTHING - do nothing
    # PROTECT - raise an error (same as RESTRICT)

    tags = models.ManyToManyField(Tag)

    # Active Record pattern
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs in {self.store.name}"