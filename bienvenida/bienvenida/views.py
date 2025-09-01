from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

def mostrar_bienvenida(request):
 nombre = "Test"
 return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")

def lista_productos(request):
 productos = Producto.objects.all()
 return render(request, 'productos/lista.html', {'productos': productos})