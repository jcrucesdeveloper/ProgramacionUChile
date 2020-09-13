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

print(azar(1,20))        
print(mayor(2,40))
