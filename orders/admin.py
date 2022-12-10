from django.contrib import admin

# Register your models here.
from orders.models import Order, Item, Item_detail


admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Item_detail)
