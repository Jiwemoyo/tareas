
import pickle 

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





f=open('practica2input/datos.bin','rb')

carro2=pickle.load(f) 

f.close()

print(carro2.caracteristicas())


