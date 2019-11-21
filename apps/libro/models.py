from django.db import models

#Autor
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    categoria = models.CharField(max_length = 220, blank = False, null = False)
    precio = models.IntegerField(default = 0)
    descripcion = models.TextField(blank = False,null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    id = models.AutoField(primary_key = True)
    comentario = models.CharField('comentario', max_length = 255, blank = False, null = False)
    fecha_de_compra = models.DateField('Fecha de publicación', blank = False, null = False)
    producto_id = models.ManyToManyField(Producto)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']

    def __str__(self):
        return self.titulo
