from functools import reduce
numeros=[0,1,2,3,4,5,6,7,8,9]

def pares(x):
    if x%2==0:
        return True
    return False

listapar=filter(pares,numeros)

def suma(x,y):
    return x+y


resultado= reduce(suma,listapar)

print(resultado)