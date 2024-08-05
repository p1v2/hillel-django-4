from django.contrib import admin

from orders.models import OrderProduct, Order


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

    fields = ('product', 'quantity', 'price')
    readonly_fields = ('price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

    list_display = ('uuid', 'user', 'total_price', 'created_at')

    fields = ('user', 'total_price')
    readonly_fields = ('total_price',)
