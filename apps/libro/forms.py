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
                    'placeholder':'Ingrese los apellidos del autor',
                    'id':'categoria'
                }
            ),
            'precio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio del producto',
                    'id':'precio'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese una pequeña descripcion del producto',
                    'id':'descripcion'
                }
            )
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario','producto_id','fecha_de_compra')
        label = {
            'comentario':'Título del libro',
            'producto_id': 'Autor(es) del Libro',
            'fecha_de_compra': 'Fecha de Publciación del Libro'
        }
        widgets = {
            'comentario': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            ),
            'producto_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_de_compra': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
