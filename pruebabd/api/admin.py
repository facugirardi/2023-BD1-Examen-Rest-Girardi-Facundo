from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Shipper)
admin.site.register(Order)
admin.site.register(OrderDetails)
