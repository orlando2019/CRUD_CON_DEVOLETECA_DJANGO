from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request):
    return render(request, "pages/inicio.html")


def index(request):
    return render(request, "pages/index.html")


def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/index.html", {"libros": libros})


def crear_libro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("libros")
    return render(request, "libros/crear.html", {"formulario": formulario})


def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    return render(request, "libros/editar.html", {"formulario": formulario})


def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect("libros")
