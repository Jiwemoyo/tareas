f=open('practica1input/cuento.txt','w')

cuento=f.write("Hola estoy creando un archivo txt de un cuento")

f.close()



f=open('practica1input/cuento.txt','r+')
cuento2 = f.read()
print(cuento2)























