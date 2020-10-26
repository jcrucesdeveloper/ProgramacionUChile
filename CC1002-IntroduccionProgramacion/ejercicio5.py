from lista import *

# suma: listaDe(n)Enteros -> int 
# devuelve la suma de los n numeros en una lista
# Ejemplos
# suma(crearLista(2,crearLista(5),listaVacia)) devuelve 7
# suma(crearLista(2,crearLista(5),crearLista(8),listaVacia)) devuelve 15

def suma(unaLista):
    if vacia(unaLista):
        return 0
    else:
        return cabeza(unaLista) + suma(cola(unaLista))

# Tests 
assert suma(crearLista(1,listaVacia)) == 1
assert suma(crearLista(2,crearLista(5,listaVacia))) == 7
assert suma(crearLista(2,crearLista(5,crearLista(8,listaVacia)))) == 15
assert not suma(crearLista(2,crearLista(2,listaVacia))) == 5

