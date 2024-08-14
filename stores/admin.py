from django.contrib import admin
from stores.models import Store


class StoreInline(admin.TabularInline):
	model = Store
	extra = 1
	fields = ('name', 'address')
	readonly_fields = ('name', 'address')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')