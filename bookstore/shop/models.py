from django.db import models
from django.contrib.auth.models import User

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Warehouse(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Product(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
