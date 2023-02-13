# sorted ordena la lista en caso de numeros de menor a mayor

lista=['z','r','y','m','e']
lista2=[7,3,2,6,8,1,3]

print(sorted(lista ,key=lambda x :str(x).startswith('e'))) # se le puede aplicar lamda para una personalizaxion
print(sorted(lista2,reverse=True))  # reverse par ordenar de maypr a menor

#imput: permite ingresar datos desde el teclado
from getpass import getpass #importacion para poner contrasena y que no se muestre

user=input("Usuario: ")
contra=input('contrasena: ')
print(f'tu edad es de {a}')

#convierte un stri a un string

numero=int(input())
numero2=int(input())

print(numero+numero2)