# -*- coding: utf-8 -*-
#Clase_13_ABB.ipynb


import estructura


#Arbol Binario
#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB","valor izq der")


# creamos un AB

ab=AB("F",\
    AB("B",\
        AB("A",None,None),\
        AB("D",\
            AB("C",None,None),\
            AB("E",None,None))),\
    AB("G",\
        None,\
        AB("I",\
            AB("H", None, None),\
            None)))



#arbol expresión
#AB con numeros en los valores de las hojas
#   y operadores en los valores de las no-hojas


ae=AB("-", \
      AB(2,None,None),\
      AB("*",\
         AB(3,None,None),\
         AB(4,None,None)))

#evaluar: AB -> num
#evalua expresión representada en AB
#ej: evaluar(ae) -> -10
def evaluar(A):

    assert type(A)==AB
    
    if A.izq==None and A.der==None: 
        return A.valor   
    
    a=evaluar(A.izq) #primer operando
    b=evaluar(A.der) #segundo operando
    op=A.valor       #operador

  
    if op=="+": 
        return a+b
    if op=="-": 
        return a-b
    if op=="*": 
        return a*b
    if op=="/": 
        return a/b

assert evaluar(ae)==-10



import estructura
#Arbol Binario
#AB: valor(any), izq(AB), der(AB)
estructura.crear("AB","valor izq der")

abb=AB("F",\
    AB("B",\
        AB("A",None,None),\
        AB("D",\
            AB("C",None,None),\
            AB("E",None,None))),\
    AB("G",\
        None,\
        AB("I",\
            AB("H", None, None),\
            None)))

#buscaValor: any AB -> bool
#True si x está en arbol
#ej: buscaValor("A",abb)->True

def buscaValor(x,arbol):
    
    assert arbol==None or type(arbol)==AB
    if arbol==None: 
        return False
      
    elif arbol.valor==x:
        return True
    elif x < arbol.valor: 
        return buscaValor(x,arbol.izq)
    elif x > arbol.valor: 
        return buscaValor(x,arbol.der)
    
assert buscaValor("A",abb)


#esABBMenor: any AB -> bool
#True AB es un ABB y todos los elementos de AB son menores que un valor
#ej: esABBMenor("F", abb2)->True

def esABBMenor(valor,arbol):
    if arbol == None:
        return True
    elif (arbol.valor < valor)\
             and esABBMenor(arbol.valor,arbol.izq)\
             and esABBMayor(arbol.valor,arbol.der):
        return True
    else:
        return False


#esABBMayor: any AB -> bool
#True AB es un ABB y todos los elementos de AB son mayores que un valor
#ej: esABBMayor("F", abb3)->True

def esABBMayor(valor,arbol):
    if arbol == None:
        return True
    elif (arbol.valor > valor) \
        and esABBMenor(arbol.valor,arbol.izq)\
        and esABBMayor(arbol.valor,arbol.der):
        return True
    else:
        return False

# Tests de esABBMenor y esABBMayor van juntos
# por que se referencian mutuamente y deben primero definirse
# y luego testearse cuando ambas estan definidas.
 
# Arbol a la derecha es abb2    
assert esABBMenor("F", AB("B",\
                            AB("A",None,None),\
                            AB("D",\
                                AB("C",None,None),\
                                AB("E",None,None))))
# Arbol a la derecha es abb3    
assert esABBMayor("F",AB("G",\
                            None,\
                            AB("I",\
                                  AB("H", None, None),\
                                  None)))

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
    
assert esABB(abb)
assert not esABB(AB("B",AB("C",None,AB("A",None,None)),None))


#escribir: AB -> None
#escribir valores de ABB A en orden ...
#ej: escribir(abb) -> ...

def escribir(arbol):
    assert arbol==None or type(arbol)==AB
    if arbol==None: 
        return
    
    escribir(arbol.izq)
    print(arbol.valor)
    escribir(arbol.der)


#insertar: any, AB -> AB
#nuevo ABB insertando x en ABB A
#ej: insertar("A",AB("B",None,None))->
#                 AB("B",AB("A",None,None),None)
def insertar(x,arbol):
   
    assert arbol==None or type(arbol)==AB
    if arbol==None: 
        return AB(x,None,None)
    
    assert x!=arbol.valor
    if x<arbol.valor: 
        return AB(arbol.valor, insertar(x,arbol.izq), arbol.der)
    if x>arbol.valor: 
        return AB(arbol.valor, arbol.izq, insertar(x,arbol.der) )

assert insertar("A",AB("B",None,None))== \
               AB("B",AB("A",None,None),None)



