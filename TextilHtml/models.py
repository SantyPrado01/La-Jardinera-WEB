from django.db import models

# Create your models here.
class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos')
    nombre = models.CharField(max_length=255)