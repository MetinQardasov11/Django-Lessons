from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    
    def __str__(self):
       return self.title