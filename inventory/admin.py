from django.contrib import admin
from inventory.models import Inventory
from products.models import Product
from django.db import models

class InventoryInline(admin.TabularInline):
	model = Inventory
	extra = 0
	fields = ('store', 'quantity')
	readonly_fields = ('store', 'quantity')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
	list_display = ('store', 'product', 'quantity',)