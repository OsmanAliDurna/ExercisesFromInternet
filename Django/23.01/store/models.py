from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField()
    
class Product(models.Model):
    name = models.CharField(max_length=50)