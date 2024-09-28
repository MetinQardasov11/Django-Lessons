from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    file_field = models.FileField(upload_to='file/products/',null=True, blank=True)
    email_field = models.EmailField(null=True, blank=True)
    bigint_field = models.BigIntegerField(null=True, blank=True)
    json_field = models.JSONField(null=True, blank=True)
    ip_field = models.GenericIPAddressField(null=True, blank=True)
    
    def __str__(self):
        return self.title