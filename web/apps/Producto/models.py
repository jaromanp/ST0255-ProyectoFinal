from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id_product = models.AutoField(primary_key = True)
    nombreP = models.CharField(max_length = 200, blank = False, null = False)
    categoria = models.CharField(max_length = 50, blank = False, null = False, default = "default")
    precio = models.IntegerField(default = 0)

    def __str__(self):
        return self.id_product

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField(null = False)
    ciudad = models.CharField(max_length = 30, blank = False, null = False)
    direccion = models.CharField(max_length = 50, blank = False, null = False)
    

    def __str__(self):
        return self.user.username


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key = True)
    id_usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comentario = models.TextField(max_length = 150)
    pub_date = models.DateField()

    def __str__(self):
        return self.id_comentario








