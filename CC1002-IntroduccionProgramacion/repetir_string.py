# repetir: str int -> str
# string x repetido n veces
# ej: repetir("ja", 3) debe ser "jajaja"
def repetir(x,n):
    assert type(x) == str and type(n) == int and n>= 0
    if n==0:
        return ""
    return x + repetir(x,n-1)

assert repetir("ja",3) == "jajaja" #caso general
assert repetir("ja",0) == "" #caso base
assert repetir("ja",1) == "ja" #caso especial
