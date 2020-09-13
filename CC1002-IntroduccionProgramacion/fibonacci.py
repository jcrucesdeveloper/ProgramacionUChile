# fibonacci: int -> int
# calcula el n-esimo numero de la sucesion de fibonacci
# ejemplo: fibonacci(7) debe dar 13

def fibonacci(n):
    assert type(n) == int and n>=0
    if n<2:
        # caso base
        return n
    else:
        # caso recursivo
        return fibonacci(n-1) + fibonacci(n-2)

# test:
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(7) == 13
