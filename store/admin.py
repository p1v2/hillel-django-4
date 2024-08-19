from django.contrib import admin

from store.models import Inventory, Store


# Register your models here.

class InventoryStoryInline(admin.TabularInline):
    model = Inventory

    fields = ('store', 'product', 'quantity')


@admin.register(Store)
class InventoryAdmin(admin.ModelAdmin):
    inlines = [InventoryStoryInline]

    list_display = ('name',)
