from django.db import models

# Create your models here.
class Product(models.Model):
    id_product = models.AutoField(primary_key = True)
    nombreP = models.CharField(max_length = 200, blank = False, null = False)
    categoria = models.CharField(max_length = 50, blank = False, null = False, default = "default")
    precio = models.IntegerField(default = 0)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True) 
    nombreUser = models.CharField(max_length = 20, blank = False, null = False)
    edad = models.IntegerField(null = False)
    ciudad = models.CharField(max_length = 30, blank = False, null = False)
    direccion = models.CharField(max_length = 50, blank = False, null = False)
    email = models.EmailField()


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key = True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField(max_length = 150)
    pub_date = models.DateField()








