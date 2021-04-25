from django.contrib import admin
from shop.models import Product, Cart, CartItem

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)