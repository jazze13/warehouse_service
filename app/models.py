from django.db import models

# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    is_our = models.BooleanField(default=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)

