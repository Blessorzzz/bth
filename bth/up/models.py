from django.db import models

# Create your models here.
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  
    sour = models.IntegerField()  # a
    sweet = models.IntegerField()  # b
    bitter = models.IntegerField()  # c
    spicy = models.IntegerField()  # d
    image = models.ImageField(upload_to='products/')  

    def __str__(self):
        return self.name
