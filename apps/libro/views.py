from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import AutorForm,LibroForm
from .models import Producto,Comentario

class Inicio(TemplateView):
    template_name = 'index.html'


class ListadoAutor(ListView):
    model = Producto
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Producto.objects.filter(estado = True)


class ActualizarAutor(UpdateView):
    model = Producto
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Producto
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Producto

    def post(self,request,pk,*args,**kwargs):
        object = Producto.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

class ListadoLibros(View):
    model = Comentario
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro:listado_libros')


class ActualizarLibro(UpdateView):
    model = Comentario
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Comentario.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Comentario

    def post(self,request,pk,*args,**kwargs):
        object = Comentario.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')
