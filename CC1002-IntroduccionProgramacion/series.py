# serieGeometrica: int -> float
# Retorna la serie geometrica de los primeros n terminos
# Ej : serieGeomtrica(5) deberia entregar 1.96875
def serieGeometrica(n):
    assert (type(n) == int) and (n>=0) # confirmamos la variable n
    if n == 0:
        return 1
    else: 
        return serieGeometrica(n-1) + 1/(2**n)

# Tests
assert serieGeometrica(5) == 1.96875
assert serieGeometrica(3) == 1.875
assert serieGeometrica(2) == 1.75
assert serieGeometrica(4) == 1.9375
# Programa principal
numero = int(input("Ingrese un nro. entero : "))
print("La suma geometrica hasta n = "+ str(numero) + " es: " + str(serieGeometrica(numero))) 
