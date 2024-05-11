from django.contrib import admin
from .models import Category, Product, Customer, Order
admin.site.register(
    [
        Category,
        Product,
        Customer,
        Order,
    ]
)
