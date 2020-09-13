# potencia :num int -> num
# calcula el valor de una potencia de base elevado a un exponente
# para exponentes enteros positivos
# ejemplo: potencia (4,5) debe dar 1024
def potencia(base,exponente): 
    
    if exponente == 0:
        return 1
    else:
        return base*(potencia(base,exponente -1))

# Funciones recursivos, deben tener un caso base y un caso "inductivo"


# digitos: int -> int
# cuenta digitos de un numero entero
# ej: digitos(245) debe ser 3
# ej: digitos(4) debe ser 1
def digitos(n):
    if abs(n) < 10:
        return 1
    else:
        return 1 + digitos(n//10)
#tests
assert digitos(245) == 3
assert digitos(-4) == 1

# factorial: int -> int
# calcula el valor factorial de n
# ejemplo: factorial(4) debe dar 24
def factorial(n):
    assert (type(n) == int) and (n>=0), "Factoria no definido para n no entero y n negativo"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#test 
assert factorial(2) == 2
assert factorial(8) == 40320

