from django.contrib import admin
from .models import Order, OrderItem,pay_status


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


class payStatusAdmin(admin.ModelAdmin):
    list_display = ['userId','email','ORDERID','amount','orderSTATUS','DATE']


admin.site.register(Order, OrderAdmin)
#admin.site.register(pay_status,payStatusAdmin)


