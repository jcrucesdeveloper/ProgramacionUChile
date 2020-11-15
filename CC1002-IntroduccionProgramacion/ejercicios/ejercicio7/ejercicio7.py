import estructura
from lista import *
from abb import *


### Funciones auxiliares ###

# unionListas: lista(any) lista(any) -> lista(any)
# devuelve lista resultado de unir dos listas
# ejemplo: unionListas(lista(1, listaVacia), lista(2, listaVacia)) 
# devuelve lista(1, lista(2, listaVacia))
def unionListas(lista1, lista2):
    if vacia(lista1):
        return lista2
    else:
        return lista(cabeza(lista1), unionListas(cola(lista1), lista2))

# Test
unaLista = lista(1, listaVacia)
otraLista = lista(2, lista(3, listaVacia))
assert unionListas(unaLista, otraLista) == lista(1, lista(2, lista(3, listaVacia)))



#esABB: AB -> bool
#True si AB es un ABB
#ej: esABB(abb)->True

def esABB(arbol):
        
    assert arbol==None or type(arbol)==AB
    if arbol==None: 
        return True

    # debemos revisar que AB izquierdo sea ABB
    if esABBMenor(arbol.valor,arbol.izq) and esABBMayor(arbol.valor,arbol.der):
            return True
    else:
        return False

def esABBMenor(valor,arbol):
    if arbol == None:
        return True
    elif (arbol.valor < valor)\
             and esABBMenor(arbol.valor,arbol.izq)\
             and esABBMayor(arbol.valor,arbol.der):
        return True
    else:
        return False
    
assert esABBMenor("F", AB("B",\
                            AB("A",None,None),\
                            AB("D",\
                                AB("C",None,None),\
                                AB("E",None,None))))


    
assert esABB(abb)
assert not esABB(AB("B",AB("C",None,AB("A",None,None)),None))

def esABBMayor(valor,arbol):
    if arbol == None:
        return True
    elif (arbol.valor > valor) \
        and esABBMenor(arbol.valor,arbol.izq)\
        and esABBMayor(arbol.valor,arbol.der):
        return True
    else:
        return False
    
assert esABBMayor("F",AB("G",\
                            None,\
                            AB("I",\
                                  AB("H", None, None),\
                                  None)))

###########

# listaAabb: lista(any) AB -> AB
# Recibe una lista y un arbol binario, y devuelve un arbol binario con sus 
# valores originales y los valores de la lista
# ejemplo: una lista con "A" "B" "C" y un AB con "F" devuelve un
# arbol binario con los valores "A", "B", "C", "F"
def listaAabb(L,A):
    assert type(L) == lista or vacia(L)
    assert esABB(A)
    if vacia(L):
        return A
    else: 
        return listaAabb(cola(L),insertar(cabeza(L),A))


# Tests
ab=AB("D",\
        AB("C",None,None),
        AB("E",None,None))
L1 = lista("A", listaVacia)
L2 = lista("F", listaVacia)
L3 = lista("G", listaVacia)

assert listaAabb(L1,ab) == AB(valor='D', izq=AB(valor='C', izq=AB(valor='A', izq=None, der=None), der=None), der=AB(valor='E', izq=None, der=None))
assert listaAabb(L2,ab) == AB(valor='D', izq=AB(valor='C', izq=None, der=None), der=AB(valor='E', izq=None, der=AB(valor='F', izq=None, der=None)))
assert listaAabb(L3,ab) == AB(valor='D', izq=AB(valor='C', izq=None, der=None), der=AB(valor='E', izq=None, der=AB(valor='G', izq=None, der=None)))




# abbAlista: AB -> lista(any) 
# Dado un ABB entrega un lista ordenada con los mismos valores
# Ejemplo: con un ab=AB("D",AB("C",None,None),AB("E",None,None))
# debe entregar una lista "C","D","E"
def abbAlista(A):
    assert esABB(A)
    if A == None:
        return  
    else:
        l1 = abbAlista(A.izq)
        valor = lista(A.valor,listaVacia)
        l2 = abbAlista(A.der)
        union_valor = unionListas(valor,l2)
        return unionListas(l1,union_valor)

        
# Tests
ab=AB("D",\
        AB("C",None,None),
        AB("E",None,None))
ab1=AB("G",\
        AB("A",None,None),
        AB("Z",None,None))
ab2=AB("B",\
        AB("A",None,None),
        AB("C",None,None))

assert abbAlista(ab) == lista("C",lista("D",lista("E",listaVacia)))
assert abbAlista(ab1) == lista("A",lista("G",lista("Z",listaVacia)))
assert abbAlista(ab2) == lista("A",lista("B",lista("C",listaVacia)))

# ordernar: lista(num) -> lista(num)
# Recibe una lista de numeros y entrega otra lista de numeros ordenados
# Ejemplo: una lista con los elementos "4" "3" "2" "1" "vacia" devuelve 
# una lista con elementos ordenados: "1" "2" "3" "4"
def ordenar(L):
    assert type(L) == lista or vacia(L)
    abb = AB(None,None,None)
    arbol = listaAabb(L,None)
    nueva_lista = abbAlista(arbol)
    return nueva_lista

# Tests
L1 = lista(4,lista(3,lista(2,lista(1,listaVacia))))
L2 = lista(1,lista(2,lista(3,lista(4,listaVacia))))
L3 = lista(2,lista(4,lista(3,lista(1,listaVacia))))

assert ordenar(L1) == lista(1,lista(2,lista(3,lista(4,listaVacia))))
assert ordenar(L2) == lista(1,lista(2,lista(3,lista(4,listaVacia))))
assert ordenar(L3) == lista(1,lista(2,lista(3,lista(4,listaVacia))))

    
    





