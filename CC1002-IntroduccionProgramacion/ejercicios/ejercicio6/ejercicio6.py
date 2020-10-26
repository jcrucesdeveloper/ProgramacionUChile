import estructura
from lista import *
from abstraccion import *

estructura.crear( "producto","nombre precio cantidad")

# funcion auxiliar para fold
# sumaProductos: num lista -> num
# suma un valor numerico con el precio de un producto 
# multiplicado por su cantidad
# ejemplo: sumaProducto(0,producto("cafe",2500,2))
# debe entregar 5000
def sumaProductos(valor,producto): 
  return valor + (producto.precio * producto.cantidad)

# siendo carrito una lista de productos.
# totalCarrito: carrito -> num
# retorna el valor de compras que contiene la lista de productos
# Ejemplo:carrito = lista(producto("cafe", 2500, 2), lista(producto("aceite", 5000, 1), None))
# totalCarrito(carrito) entrega 10000
def totalCarrito(unaLista):
  return fold(sumaProductos,0,unaLista)


# Programa principal
carrito = lista(producto("cafe", 2500, 2), lista(producto("aceite", 5000, 1), None))
print (totalCarrito(carrito))
