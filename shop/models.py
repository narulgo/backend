from django.db import models
from datetime import datetime


class Product(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=7, decimal_places=2)
    product_num = models.IntegerField()
    description = models.CharField(max_length=200)
    inStock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.total_price = sum(item.product.price * item.amount for item in self.items.all())
        super().save(*args, **kwargs)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.save()