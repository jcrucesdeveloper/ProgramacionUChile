# Modulo para ser implementado en tarea2.py
import estructura
from lista import *
from abstraccion import *

estructura.crear("resultadoMesa","circunscripcion mesa apruebo rechazo")

# buscaMesa: lista(resultadoMesa) str num -> resultadoMesa
# Busca una mesa dentro de una lista de mesas
# Ejemplo: siendo L una lista de mesas,
# si buscamos buscaMesa(L,"San Miguel",2) debe entregar resultadoMesa("San Miguel",2,200,60)
def buscaMesa(L,circu,num_mesa):
    assert type(L) == lista or L == listaVacia
    assert type(circu) == str
    assert type(num_mesa) == int

    if vacia(L):
        return None
    else:
        if cabeza(L).circunscripcion == circu and cabeza(L).mesa == num_mesa:
            return cabeza(L)
        else: 
            return buscaMesa(cola(L),circu,num_mesa)
# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
L = crearLista(r1,crearLista(r2,listaVacia))
assert buscaMesa(L,"Santiago",3) == resultadoMesa("Santiago",3,100,20)
assert buscaMesa(L,"San Miguel",2) == resultadoMesa("San Miguel",2,200,60)
assert buscaMesa(L,"Quilicura",32) == None


# agregaMesa: lista(resultadoMesa) resultadoMesa -> lista(resultadoMesa)
# agrega un resultado mesa al inicio de una lista de resultados mesa
# si el resultado mesa que se intenta agregar ya se encuentra en la lista
# simplemente retornamos la lista inicial
# Ejemplo: 
# r1 = resultadoMesa("Santiago",3,100,20)
# r2 = resultadoMesa("San Miguel",2,200,60)
# r3 = resultadoMesa("Putre",23,331232,1)
# L = crearLista(r1,crearLista(r2,listaVacia))
# agregaMesa(L,r3) debe devolver una lista con r3,r1,r2 en ese orden
#####
def agregaMesa(L,r):
    assert type(L) == lista or L == listaVacia
    assert type(r) == resultadoMesa

    if buscaMesa(L,r.circunscripcion,r.mesa):
        return L
    else:
        return crearLista(r,L)
# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
r3 = resultadoMesa("Putre",23,331232,1)
L = lista(r1,listaVacia)
assert agregaMesa(L,r2) == lista(resultadoMesa("San Miguel",2,200,60),lista(resultadoMesa("Santiago",3,100,20),listaVacia))
assert agregaMesa(L,r3) == lista(resultadoMesa("Putre",23,331232,1),lista(resultadoMesa("Santiago",3,100,20),listaVacia))
assert agregaMesa(L,r1) == lista(resultadoMesa("Santiago",3,100,20),listaVacia)


# funcion auxiliar para mesaConMasVotos
def mayor(r1,r2):
    assert type(r1) == type(r2) == resultadoMesa
    return (r1.apruebo + r1.rechazo) > (r2.apruebo + r2.rechazo)

# mesaConMasVotos: lista(resultadoMesa) -> resultadoMesa
# devuelve la mesa con mas votos dentro de una lista de mesas
# Ejemplo: mesaConMasVotos(lista(resultadoMesa("Santiago",3,100,20),lista(resultadoMesa("San Miguel",2,200,600),listaVacia))) debe 
# devolver resultadoMesa("San Miguel",2,200,600)
def mesaConMasVotos(L):
    assert type(L) == lista or L == listaVacia

    if vacia(L):
        return None
    else:
        if filtro(mayor,cola(L),cabeza(L)) == listaVacia:
            return cabeza(L)
        else:
            return mesaConMasVotos(cola(L))
# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
r3 = resultadoMesa("Putre",23,331232,1)

L1 = lista(r1,listaVacia)
L2 = lista(r1,lista(r2,listaVacia))
L3 = lista(r1,lista(r2,lista(r3,listaVacia)))
assert mesaConMasVotos(L1) == resultadoMesa("Santiago",3,100,20)
assert mesaConMasVotos(L2) == resultadoMesa("San Miguel",2,200,60)
assert mesaConMasVotos(L3) == resultadoMesa("Putre",23,331232,1)

# funcion auxiliar para resultadosCircunscripcion
def circun_igual(c1,c2):
    assert type(c1) == resultadoMesa
    assert type(c2) == str

    return c1.circunscripcion == c2

# resultadosCircunscripcion: lista(resultadosMesa) str -> lista(resultadosMesa)    
# filtra los valores de una lista de mesas utilizando la circunscripcion
# Ejemplo: si L contiene 4 mesas y 2 de ellas son de Paine
# utilizando resultadosCircunscripcion(L,"Paine") debe devolver una lista de largo 2
# incluyendo solo las mesas de Paine
def resultadosCircunscripcion(L,circunscripcion):
    assert type(L) == lista or L == listaVacia
    assert type(circunscripcion) == str

    return filtro(circun_igual, L, circunscripcion)
# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
r3 = resultadoMesa("Putre",23,331232,1)
r4 = resultadoMesa("Santiago",21,10,0)
r5 = resultadoMesa("Putre",203,10,0)

L = lista(r1,lista(r2,lista(r3,lista(r4,lista(r5,listaVacia)))))
assert resultadosCircunscripcion(L,"Putre") == lista(resultadoMesa("Putre",23,331232,1),lista(resultadoMesa("Putre",203,10,0),listaVacia))
assert resultadosCircunscripcion(L,"Santiago") == lista(resultadoMesa("Santiago",3,100,20),lista(resultadoMesa("Santiago",21,10,0),listaVacia))
assert resultadosCircunscripcion(L,"San Miguel") == lista(resultadoMesa("San Miguel",2,200,60),listaVacia)


# funcion auxiliar para totalesVotosFinales
def mapeoApruebo(L):
    return L.apruebo

# funcion auxiliar para totalesVotosFinales
def mapeoRechazo(L):
    return L.rechazo

# funcion auxiliar para totalesVotosFinales
def suma(x,y):
    return x+y

# totalesVotosFinales: lista(resultadosMesa) str -> num
# Recibe una lista y una postura de votacion (Apruebo o Rechazo)
# y devuelve le numero de votos obtenidos de dicha opcion
# Ejemplo: totalVotosFinales(lista(resultadoMesa("Santiago",42,20, 30),lista(resultadosMesa("Santiago",30,30,20),listaVacia)),"Apruebo")
# debe devolver la suma de los votos del apruebo: 50
def totalVotosFinales(L,votacion):
    assert type(L) == lista or L == listaVacia
    assert type(votacion) == str
    assert votacion == "Apruebo" or votacion == "Rechazo"

    if votacion == "Apruebo":
        L_mapeada = mapa(mapeoApruebo,L)
    else: 
        L_mapeada = mapa(mapeoRechazo,L)
    return fold(suma,0,L_mapeada)

# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
r3 = resultadoMesa("Putre",23,200,1)
r4 = resultadoMesa("Santiago",42,200,30)

L = lista(r1,lista(r2,lista(r3,lista(r4,listaVacia))))
assert totalVotosFinales(L,"Apruebo") == 700
assert totalVotosFinales(L,"Rechazo") == 111

    
# totalesPorCircunscripcion: lista(resultadosMesa) str str -> num
# Devuelve el total de votos del apruebo o del rechazo de una
# circunscripscion especifica
# Ejemplo: si tenemos 4 mesas (resultadosMesa) en una lista
# y buscamos los votos de Santiago que son apruebo
# totalesPorCircunscripcion(Lista,"Santiago","Apruebo") 
# debe entregar las sumatoria de esos votos
def totalesPorCircunscripcion(L,circunscripcion,votacion):
    assert type(L) == lista or L == listaVacia
    assert type(circunscripcion) == str
    assert type(votacion) == str
   
    L_filtrada = resultadosCircunscripcion(L,circunscripcion)
    return totalVotosFinales(L_filtrada,votacion)
# Tests
r1 = resultadoMesa("Santiago",3,100,20)
r2 = resultadoMesa("San Miguel",2,200,60)
r3 = resultadoMesa("Putre",23,331232,1)
r4 = resultadoMesa("Santiago",42,200,30)

L = lista(r1,lista(r2,lista(r3,lista(r4,listaVacia))))
assert totalesPorCircunscripcion(L,"Santiago","Apruebo") == 300
assert totalesPorCircunscripcion(L,"Santiago","Rechazo") == 50
assert totalesPorCircunscripcion(L,"San Miguel","Rechazo") == 60

