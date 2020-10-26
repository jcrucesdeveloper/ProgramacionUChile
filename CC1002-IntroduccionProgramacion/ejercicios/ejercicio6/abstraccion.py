from lista import *


#Lo importante de este modulo de este modulo es que posee:

#1. funcion mapa: aplica funcion a todos los elementos de una lista

#2. funcion filtro: entrega lista con elementos que cumplen lo evaluado
#   en una funcion

#3. funcion fold: se reduce lista a un resultado calculado por una funcion
#   que opera los elementos de la lista

# filtro :  (Y X -> bool) lista(X) Y -> lista(X)
# devuelve lista con todos los valores donde operador devuelve True
def filtro(funcion, unaLista, n):
    if vacia(unaLista):
        return listaVacia 
    else:
        if (funcion(cabeza(unaLista),n)):
            return crearLista(cabeza(unaLista),filtro(funcion, cola(unaLista),n))
        else:
            return filtro(funcion,cola(unaLista),n)
        
# Tests
valores = lista(6, lista(4, lista(8, listaVacia)))
assert filtro(lambda x,y: x < y, valores,5) == lista(4, listaVacia) 

# filtro :  (X -> bool) lista(X) -> lista(X)
# devuelve lista con todos los valores donde operador devuelve True
def filtro(funcion, unaLista):
    if vacia(unaLista):
        return listaVacia 
    else:
        if (funcion(cabeza(unaLista))):
            return crearLista(cabeza(unaLista),filtro(funcion, cola(unaLista)))
        else:
            return filtro(funcion,cola(unaLista))
        
# Tests
valores = lista(6, lista(4, lista(8, listaVacia)))
assert filtro(lambda x: x < 5, valores) == lista(4, listaVacia) 

# mapa : (X -> Y) lista(X) -> lista(Y)
# devuelve lista con funcion aplicada a todos sus elementos
def mapa(f, unaLista): 
    if vacia(unaLista): 
        return listaVacia
    else:
        return crearLista(f(cabeza(unaLista)), mapa(f, cola(unaLista)))          

# Tests
valores = lista(1, lista(2, lista(3, lista(4, listaVacia)))) 
assert mapa(lambda x: 10*x, valores) == \
            lista(10, lista(20, lista(30, lista(40, listaVacia)))) 
valores = lista("pedro", lista("juan", lista("diego", listaVacia)))
assert mapa(lambda x: x.upper(), valores) == \
            lista("PEDRO", lista("JUAN", lista("DIEGO", listaVacia)))

# fold: (X X -> X) X lista(X) -> X
# procesa la lista con la funcion f y devuelve un unico valor
# el valor init se usa como valor inicial para procesar el primer
# valor de la lista y como acumulador para los resultados
# parciales
# pre-condicion: la lista debe tener al menos un valor

def fold(f, init, unaLista):
    if vacia(cola(unaLista)): # un solo valor
        return f(init, cabeza(unaLista))
    else:
        return fold(f, f(init, cabeza(unaLista)), cola(unaLista))

# Tests
valores = lista(1, lista(2, lista(3, lista(4, listaVacia))))
assert fold(lambda x, y: x + y, 0, valores) == 10
valores = lista("pedro", lista("juan", lista("diego", listaVacia))) 
assert fold(lambda x, y: x + y, "", valores) == "pedrojuandiego"

