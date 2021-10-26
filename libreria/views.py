from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "pages/inicio.html")


def index(request):
    return render(request, "pages/index.html")


def libros(request):
    return render(request, "libros/index.html")


def crear_libro(request):
    return render(request, "libros/crear.html")


def editar_libro(request):
    return render(request, "libros/editar.html")
