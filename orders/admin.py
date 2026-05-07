from django.contrib import admin
from .models import OrderItem, Total

admin.site.register(Total)
admin.site.register(OrderItem)
