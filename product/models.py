from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default='')
