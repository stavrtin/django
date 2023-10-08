from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    user_created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'User {self.name}'

class Product(models.Model):
    prodname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.FloatField()
    date_added_prod = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Product {self.prodname}'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    create_order_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Order {self.pk} {self.customer} {self.products}  {self.total}\n '