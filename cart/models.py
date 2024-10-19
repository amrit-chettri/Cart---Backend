from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='product/images', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s cart'
