# Evaluacion de expresiones
print(3+5)
print(3+2*5)
print((3+2)*5)
print(2**3)
print(4**0.5)
print(10%3)
print('abra' + 'cadabra')
print('ja'*3)
print(1+2)
print(1.0+2.0)
print(1.0+2)
print(1/2)
print(1//2)
print(1.0//2.0)
print('En el curso hay ' + str(30) + ' alumnos')
print('100'+'1')
print(int('100') +1)

# Variables
a = 8 # la variable contiene el valor 8
b = 12 # la variable contiene el valor 12
print(a)
print(a+b)
c = a + 2 * b #creamos una expresion, se evalua y define c
print(c)
a = 10 #redefinimos a
print(c) # el valor de c no cambia

# Usar nombre descriptivos para variables
a = 8
b = 12 
c = a * b
#  Mejor:
ancho = 8
largo = 12
area = ancho * largo
print(area)

dia = '12'; mes = 'marzo'; agno = '2018'
hoy = dia + ' de ' + mes + ' de '+ agno
print(hoy)

# Errores
'''
No incluidos directamente para que el programa corra

# Errores de tipo
dia = 13
mes = 'marzo'
print('Hoy es ' + dia + ' de ' + mes) # Mes es tipo int
# solucion
print('Hoy es ' + str(dia) + ' de ' + mes) # Transformamos a string

# Errores de identacion 
x = 3
    x #tiene un 'tab' de diferencia' 

# Errores de sintaxis

numero = 15 
antecesor = (numero -1)) # Un ) de mas

# Errores de nombre 
lado1 = 15

area = lado1/lado2 # lado2 no definido

'''
