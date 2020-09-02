pi = 3.14

# areaCirculo: num -> num
# Calcula el area de un circulo utilizando su radio
# ejemplo: areaCirculo(2) debe producir 12.56

def areaCirculo(r):
    return pi*r**2

# Test
assert areaCirculo(2) == 12.56

# areaAnillo num num -> num
# Calcula el area de un anillo utilizando el radio exterior e interior
# ejemplo: areaAnillo(4,2) debe producir  37.68

def areaAnillo(r_exterior,r_interior):
    return areaCirculo(r_exterior) - areaCirculo(r_interior)

# Test
assert areaAnillo(4,2) == 37.68

# perimetroCirculo: num -> num
# Calcula el perimetro de un circulo utilizando su radio
# ejemplo : perimetroCirculo(3) debe producir 18.84

def perimetroCirculo(r):
    return 2 * pi * r

# Test
assert perimetroCirculo(3) == 18.84

# perimetroAnillo(r_exterior, r_interior):
# Calcula el perimetro de un anillo utilizando el radio exterior e interior
# ejemplo: perimetroAnillo(4,6) debe producir 62.8 

def perimetroAnillo(r_exterior,r_interior):
    return perimetroCirculo(r_exterior) + perimetroCirculo(r_interior)

# Test
assert perimetroAnillo(4,6) == 62.8
