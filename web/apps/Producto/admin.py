from django.contrib import admin
from .models import Product
from .models import Usuario
from .models import Comentario

admin.site.register(Product)
admin.site.register(Usuario)
admin.site.register(Comentario)

