# calculaListaFactoriales: None -> NOne
# calcular factorial de lista de numeros ingresadas por teclado
# la lista termina con el valor fin
# ej: factoriales()

from funcionRecursiva import factorial
def calculaListaFactoriales():
    respuesta = input('n ?')
    if respuesta == "fin":
        return
    # caso no es igual a fin
    n = int(respuesta)
    factorial_n = factorial(n)
    print(str(n) + '!=' + str(factorial_n))
    calculaListaFactoriales()

calculaListaFactoriales()
