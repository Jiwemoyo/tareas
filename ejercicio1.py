paises=[]


while len(paises) < 5:
    paises.append(input("ingresa un pais: "))

ListaF=sorted(set(paises))

print(ListaF)
