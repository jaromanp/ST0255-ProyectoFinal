from django import forms
from .models import Producto,Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','categoria','precio','descripcion']
        labels = {
            'nombre': 'Nombre del autor',
            'categoria': 'Categoria del producto',
            'precio': '¿Cuanto costo tu producto?',
            'descripcion': 'Pequeña descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del producto',
                    'id': 'nombre'
                }
            ),
            'categoria': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la categoria del instrumento',
                    'id':'categoria'
                }
            ),
            'precio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio del producto',
                    'id':'precio'
                }
            )
            
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('titulo','comentario','producto_id','fecha_de_compra')
        label = {
            'Titulo':'titulo',
            'comentario':'comentario',
            'producto_id': 'productos relacionados al comentario',
            'fecha_de_compra': 'Fecha en la que compro el producto'
        }
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el titulo de comentario max 30 caracteres',
                    'id':'titulo'
                }
            ),
            'comentario': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese su comentario',
                    'id':'descripcion'
                }
            ),
            'producto_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            )
            ,
            'fecha_de_compra': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
