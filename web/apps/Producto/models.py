from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoFiel(primary_key = True)
    nombre = models.CharField(max_lenght = 200, blank = False, null = False)