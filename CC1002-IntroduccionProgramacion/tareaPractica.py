# Modulos 
from triangulo import *
import math
import random

def azar(x,y):
    return random.randint(x,y)

def mayor(x,y):
    if x > y: 
        return x
    else: 
        return y

def esPar(x):
    if x % 2 == 0:
        return True
    else: 
        return False

print(esPar(400))
print(azar(1,20))        
print(mayor(2,40))

