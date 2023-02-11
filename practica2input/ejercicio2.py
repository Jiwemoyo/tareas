#guardar un objeto en un fichero para poder recuperarlos
#serializar: convertir una representacion de un programa a una secuenciade datos que se pueden entender en un fichero
#deserializar: tomar una secuancia de datos y converirlo en un programa legible (lo contrario de serializar)
import pickle #permite serializar

class Vehiculo:
    color=""
    modelo=""
    precio=0
    
    def __init__(self,color,modelo,precio):
        self.color=color
        self.modelo=modelo
        self.precio=precio

    def caracteristicas(self):
        return f"vehiculo de color {self.color} modelo {self.modelo} con un precio de {self.precio}"



# auto1=Vehiculo('rojo','nuevo',200000)

# f=open('practica2input/datos.bin','wb')

# pickle.dump(auto1,f) #prime parametro lo que quiero seializar , segunof parametro donde lo voy a serializar

# f.close()

f=open('practica2input/datos.bin','rb')

carro2=pickle.load(f)

f.close()


print(carro2.caracteristicas())


