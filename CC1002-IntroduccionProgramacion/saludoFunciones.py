# buenosDias: int -> bool
# Recibe una hora del dia y dice si corresponde a la manana o no (entre 1 <= x <12)
# Ej: buenosDias(12) devuelve False
def buenosDias(hora):
    if hora >= 1 and hora < 12:
        return True
    else:
        return False
# tests
assert buenosDias(1) == True 
assert buenosDias(12) == False 
assert buenosDias(11) == True
assert buenosDias(21) == False

# buenasTardes: int -> bool
# Recibe una hora del dia y dice si corresponde a la tarde o no
# Ej : buenasTardes(12) devuelve True, buenasTardes(21) devuelve False
def buenasTardes(hora):
    if hora >= 12 and hora <21:
        return True
    else:
        return False

# Tests
assert buenasTardes(12) == True 
assert buenasTardes(21) == False
assert buenasTardes(16) == True
assert buenasTardes(9) == False

