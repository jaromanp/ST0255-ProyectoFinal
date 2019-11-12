from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)


def __str__(self):
    return self.nombre