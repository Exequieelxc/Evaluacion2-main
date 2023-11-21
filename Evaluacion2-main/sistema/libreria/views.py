from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from .models import Biblioteca


def biblioteca(request):
    biblioteca = Biblioteca.objects.first()
    return render(request, 'paginas/biblioteca.html', {'biblioteca': biblioteca})

def nosotros(request):
    return render (request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render (request, 'Libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render (request, 'Libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render (request, 'Libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def biblioteca_detail(request):
    biblioteca = Biblioteca.objects.first()  # Obtén la primera biblioteca (puedes ajustar esto según tu lógica)
    return render(request, 'biblioteca_detail.html', {'biblioteca': biblioteca})
