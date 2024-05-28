from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prototal= models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return self.name


