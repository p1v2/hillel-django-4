from django.contrib import admin

from products.models import Product, Category, Tag, Store, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Store)
admin.site.register(Inventory)
