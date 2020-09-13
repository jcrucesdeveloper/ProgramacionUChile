# saludo: int -> str
# Determinar el saludo de acuerdo a la hora del dia 1 <= hora <= 24 
# ejemplos: saludo(11) debe devolver Buenos dias!
# saludo(15) debe devolver Buenas tardes
from saludoFunciones import *

def saludo(hora):
    if buenosDias(hora):
        return 'Buenos dias!'
    elif buenasTardes(hora):
        return 'Buenas tardes!'
    else: 
        return 'Buenas noches!'
# test:
# probar condiciones de Borde (o limites): 1hrs, 12hrs, 21hrs, 24hrs
assert saludo(1) == 'Buenos dias!'
assert saludo(11) == 'Buenos dias!'
assert saludo(12) == 'Buenas tardes!'
assert saludo(15) == 'Buenas tardes!'
assert saludo(21) == 'Buenas noches!'
assert saludo(23) == 'Buenas noches!'
assert saludo(24) == 'Buenas noches!'
