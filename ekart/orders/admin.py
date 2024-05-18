from django.contrib import admin
from.models import Payment, Order, OrderProduct

# Register your models here.


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'order_total', 'status', 'is_ordered', 'created_at']
    inlines = [OrderProductInline]


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)