# hanoi: int -> int
# calcula el numero de movimientos necesarios aara mover 
# una torre de n discos de una vara a otra
# usando 3 varas y siguiendo las restricciones del puzzle hanoi
# ejemplo: hanoi(0) debe dar 0, hanoi(1) debe dar 1, hanoi(2) debe dar 3
def hanoi(n):
    if n < 2:
        return n
    else:
        return 1+ 2* hanoi(n-1)

#test
assert hanoi(0) == 0 
assert hanoi(1) == 1 
assert hanoi(4) == 15
assert hanoi(5) == 31
