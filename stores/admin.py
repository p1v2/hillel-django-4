from django.contrib import admin
from stores.models import Store
from inventory.models import Inventory

class InventoryInline(admin.TabularInline):
	model = Inventory
	extra = 1
	fields = ('product', 'quantity')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	inlines = [InventoryInline]