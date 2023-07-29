from django.shortcuts import render
from .models import product

# Create your views here.
def ObjetoTienda(request):
    obj = product.objects.all()
    categorias = []
    for producto in obj:
        if producto.categoria not in categorias :
            categorias.append(producto.categoria)
    context ={
      'productos': obj,
      'categorias': categorias,
    }
    return render(request, 'almacen/index.html', context)

def obtener_productos(request):
    categoria = request.GET.get('categoria')
    if categoria == 'Todos':
        productos = product.objects.all()
    else:
        productos = product.objects.filter(categoria=categoria)
    context = {
        'productos': productos
    }
    return render(request, 'almacen/productos.html', context)