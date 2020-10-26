import random
# codificaJugada: str -> int
# Recibe un string y devuelve el codigo numero correspondiente a la jugada
# Ej: codificaJugada('tijeras') debe otorgar 0
def codificaJugada(jugada):
    if jugada == 'tijeras':
        return 0
    elif jugada == 'papel':
        return 1
    elif jugada == 'piedra':
        return 2
    elif jugada == 'lagarto':
        return 3
    elif jugada == 'spock':
        return 4
    else:
        return -1

# Tests
assert codificaJugada('tijeras') == 0
assert codificaJugada('papel') == 1
assert codificaJugada('piedra') == 2
assert codificaJugada('lagarto') == 3
assert codificaJugada('spock') == 4
assert codificaJugada('error') == -1

# decodificaJugada: int -> string
# Recibe un entero y devuelve un string con el nombre de la jugada correspondiente
def decodificaJugada(numero_jugada):
    if numero_jugada == 0:
        return 'tijeras'
    elif numero_jugada == 1:
        return 'papel'
    elif numero_jugada == 2:
        return 'piedra'
    elif numero_jugada == 3:
        return 'lagarto'
    elif numero_jugada == 4:
        return 'spock'
    else:
        return ""

# Tests
assert decodificaJugada(0) == 'tijeras'
assert decodificaJugada(1) == 'papel'
assert decodificaJugada(2) == 'piedra'
assert decodificaJugada(3) == 'lagarto'
assert decodificaJugada(4) == 'spock'
assert decodificaJugada(231) == ''

# ganaJugada: int int -> int
# Recibe valores correspondientes a las jugadas y devuelve: valor 1 si gana el jugador 1; valor 0 si hay empate; valor -1 si gana el jugador 2
# Ej: ganaJugada(0,4) devuelve -1
def ganaJugada(jugada1,jugada2):
    if jugada1 == jugada2:
        return 0
    elif jugada1 == 0 and jugada2 == 3:
        return 1
    elif jugada1 == 3 and jugada2 == 0:
        return -1
    elif jugada1 == 1 and jugada2 == 4:
        return 1
    elif jugada1 == 4 and jugada2 == 1:
        return -1
    elif jugada1 == 2 and jugada2 == 0:
        return 1
    elif jugada1 == 0 and jugada2 == 2:
        return -1
    elif jugada1 == 3 and jugada2 == 1:
        return 1
    elif jugada1 == 1 and jugada2 == 3:
        return -1
    elif jugada1 == 4 and jugada2 == 2:
        return 1
    elif jugada1 == 2 and jugada2 == 4:
        return -1
    elif jugada1 == 4 and jugada2 == 0:
        return 1
    elif jugada1 == 0 and jugada2 == 4:
        return -1
    elif jugada1 > jugada2:
        return 1
    else:
        return -1

# Tests
assert ganaJugada(0,4) == -1
assert ganaJugada(2,0) == 1
assert ganaJugada(2,2) == 0
assert ganaJugada(2,0) == 1
assert ganaJugada(3,1) == 1

# justificaResultado: int int -> string
# Recibe dos numeros correspondiente la jugada de los jugadores, devuelve un string que justifica el resultado
# Ej: justificaResultado(3,4) devuelve 'lagarto envenena a spock'
def justificaResultado(jugada1,jugada2):
    if jugada1 == jugada2:
        return "Empate"
    if (jugada1 == 0 and jugada2 == 1) or (jugada1 == 1 and jugada2 == 0):
        return 'tijeras cortan papel'
    if (jugada1 == 1 and jugada2 == 2) or (jugada1 == 2 and jugada2 == 1):
        return 'papel cubre piedra'
    if (jugada1 == 2 and jugada2 == 3) or (jugada1 == 3 and jugada2 == 2):
        return 'piedra aplasta lagarto'
    if (jugada1 == 3 and jugada2 == 4) or (jugada1 == 4 and jugada2 == 3):
        return 'lagarto envenena a spock'
    if (jugada1 == 4 and jugada2 == 0) or (jugada1 == 0 and jugada2 == 4):
        return 'spock destruye tijeras'
    if (jugada1 == 0 and jugada2 == 3) or (jugada1 == 3 and jugada2 == 0):
        return 'tijeras decapitan lagarto'
    if (jugada1 == 3 and jugada2 == 1) or (jugada1 == 1 and jugada2 == 3):
        return 'lagarto come papel'
    if (jugada1 == 1 and jugada2 == 4) or (jugada1 == 4 and jugada2 == 1):
        return 'papel refuta spock'
    if (jugada1 == 4 and jugada2 == 2) or (jugada1 == 2 and jugada2 == 4):
        return 'spock vaporiza piedra'
    if (jugada1 == 2 and jugada2 == 0) or (jugada1 == 0 and jugada2 == 2):
        return 'piedra aplasta tijera'
    else: 
        return "ERROR"
# Tests
assert justificaResultado(3,4) == 'lagarto envenena a spock'
assert justificaResultado(1,4) == 'papel refuta spock'
assert justificaResultado(3,1) == 'lagarto come papel'
assert justificaResultado(2,0) == 'piedra aplasta tijera'

# generaJugadaJugador: None -> int
# Genera jugada de manera aleatoria con valores entre 0 y 4
# Ej: generaJugadaJugador() puede devolver 3
def generaJugadaComputador():
    return random.randint(0,4)

# Tests
assert generaJugadaComputador() >= 0
assert generaJugadaComputador() <= 4
