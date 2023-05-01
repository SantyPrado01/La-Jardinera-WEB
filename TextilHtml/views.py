from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos':productos})

def nosotros(request):
    return render(request, 'sobre_nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')