from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from .models import Biblioteca
from .models import Proveedor
from .forms import ProveedorForm



def biblioteca(request):
    biblioteca = Biblioteca.objects.first()
    return render(request, 'paginas/biblioteca.html', {'biblioteca': biblioteca})

def proveedor(request):
    return render (request, 'paginas/proveedor.html')

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
    biblioteca = Biblioteca.objects.first() 
    return render(request, 'biblioteca_detail.html', {'biblioteca': biblioteca})

def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()

    return render(request, 'proveedor/registrar_proveedor.html', {'form': form})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def proveedor_lista(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/proveedor_lista.html', {'proveedores': proveedores})

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedor/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('lista_proveedores')