from django.contrib import admin
from products.models import Product, Category, Tag
from inventory.models import Inventory
from django.db import models


class IventoryInline(admin.TabularInline):
	model = Inventory
	extra = 0
	fields = ('store', 'quantity')
	readonly_fields = ('store', 'quantity')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'total_quantity',)
	inlines = [IventoryInline]
	
	def total_quantity(self, obj):
		return Inventory.objects.filter(product=obj).aggregate(total=models.Sum('quantity'))['total']
	
	total_quantity.short_description = 'Total Quantity'


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
