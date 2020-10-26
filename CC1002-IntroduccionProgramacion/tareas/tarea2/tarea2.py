import estructura
from lista import *
from abstraccion import *
from estadisticas import *

# Funciones Auxiliares

def obtenerResultados(L):
    circunscripcion = input("Circunscripcion (o 'fin' para terminar): ")
    if circunscripcion == "fin":
        return L 
    else: 
        num_mesa = int(input("Numero de la mesa: "))
        votos_apruebo = int(input("Numero de votos opcion 'Apruebo': "))
        votos_rechazo = int(input("Numero de votos opcion 'Rechazo': "))
        mesaNueva = resultadoMesa(circunscripcion, num_mesa, votos_apruebo,votos_rechazo)
        listaDeResultados = agregaMesa(L, mesaNueva)
        return obtenerResultados(listaDeResultados)

def imprimirEstadisticasBasicas(L):
    print("Estadisticas Basicas")
    print("Total Plebiscito Constituyente")
    print("Total Opcion Apruebo: %s" % (totalVotosFinales(L,"Apruebo")) )
    print("Total Opcion Rechazo: %s\n" % (totalVotosFinales(L,"Rechazo")) )

def imprimirEstadisticasAvanzadas(L):
    mayorM = mesaConMasVotos(L)
    sumaDeVotos = mayorM.apruebo + mayorM.rechazo
    print("Mesa con mas concurrencia: %s, mesa %s, con %s votantes.\n" % \
            (mayorM.circunscripcion,mayorM.mesa,sumaDeVotos))

def infoParticular(L,mesaParticular):
    totalApruebo = totalesPorCircunscripcion(L,mesaParticular,"Apruebo") 
    totalRechazo = totalesPorCircunscripcion(L,mesaParticular,"Rechazo") 
    print("Votacino en Circunscripcion %s: " % (mesaParticular))
    print("Apruebo: %s, Rechazo: %s." % (totalApruebo,totalRechazo))

# Programa Principal
print("Bienvenido al sistema de estadiscticas Plebiscito Constituyente 2020.")
print("Ingrese los resultados por mesa")
resultados = obtenerResultados(listaVacia)
imprimirEstadisticasBasicas(resultados)
imprimirEstadisticasAvanzadas(resultados)

mesaParticular = input("Circunscripsion de su interes: ")
infoParticular(resultados,mesaParticular)







