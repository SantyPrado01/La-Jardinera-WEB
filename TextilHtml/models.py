from django.db import models

# Create your models here.
class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos')
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=8, decimal_places=2)