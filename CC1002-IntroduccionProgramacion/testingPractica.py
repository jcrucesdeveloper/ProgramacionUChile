# Testing, depuracion y recursion 
# Testing: Acciones que permiten probar laf ucnional del programa
# Dpuracion: Proceso de detectar y corregir errores en un programa 
# Errores logicos: aquellos que causan que nuestro programa no calcule lo deseado 

# Testing de funciones:
#   - Debe cumplir con el contrato estipulado en la recta de diseno
#   - Se debe utilizar hartos test para que se cumplan lo que la funcion quiere hacer
#   - Un buen testing: casos de borde y uno representativo

# Ejemplos

# suma: int int ->
# Calcula x + ( x+1) + ... +y
# ej : suma(3,5) debe ser 12
def suma(x,y):
    assert (type(x) == int) and (type(y) == int)
    if x > y:
        return 0
    else:
        return x + suma (x+1, y)

print(suma(3,5))
assert suma(3,5) == 12
assert suma(3,3) == 3
assert suma(5,3) == 0
