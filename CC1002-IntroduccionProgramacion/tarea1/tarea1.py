# Tarea numero 1: Modulos y Condiciones

# Jugar: None -> None (Recursiva)
# Sirve para comenzar una nueva partida de cachipunLS
# Ej: jugar() comenzara una partida
from cachipunLS import *

def jugar():

    print('Bienvenido al juego de cahipun-lagarto-spock!!!')
    print('Ingrese la modalidad en que quiere jugar')
    modalidad = int(input('jugador vs. computador (1) o computador vs. computador (2): '))
    if modalidad == 1:
        print('modalidad elegida Jugador vs. Computador')
        jugada_jugador_str = input("Jugador 1 ingrese jugada ['papel'|'tijeras'|'piedra'|'lagarto'|'spock']: ")
        jugada_jugador = codificaJugada(jugada_jugador_str)
        jugada_computadora = generaJugadaComputador()
        print('Jugador 2 (computador) juega ' + decodificaJugada(jugada_computadora))
        ganador = ganaJugada(jugada_jugador,jugada_computadora)
        
        if ganador == 1:
            justificacion = justificaResultado(jugada_jugador,jugada_computadora)
            print('Gana jugador 1!! ' + justificacion)
        elif ganador == -1:
            justificacion = justificaResultado(jugada_computadora,jugada_jugador)
            print('Gana jugador 2!! '+ justificacion)
        else: 
           opcion = int(input('Empate, te gustaria jugar denuevo? (1) Si (2) No : '))
           if opcion == 1:
               jugar()
    else:
        print('modalidad elegida Computador vs. Computador')
        computadora1 = generaJugadaComputador()
        computadora2 = generaJugadaComputador()
        print('Jugador 1 (Computadora) juega ' + decodificaJugada(computadora1))
        print('Jugador 2 (Computadora) juega ' + decodificaJugada(computadora2))
        ganador = ganaJugada(computadora1,computadora2)

        if ganador == 1:
            justificacion = justificaResultado(computadora1,computadora2)
            print('Gana jugador 1!! ' + justificacion)
        elif ganador == -1:
            justificacion = justificaResultado(computadora2,computadora1)
            print('Gana jugador 2!! '+ justificacion)
        else: 
           opcion = int(input('Empate, te gustaria jugar denuevo? (1) Si (2) No : '))
           if opcion == 1:
               jugar()

jugar()
