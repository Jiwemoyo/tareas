class Vehiculo:
    def __init__(self,color,ruedas,puerta):
        self.color=color
        self.ruedas=ruedas
        self.puerta=puerta

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puerta,velocidad,cilindrada):
        super().__init__(color, ruedas, puerta)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def descripcion(self):
        return f"{self.color} {self.ruedas} {self.puerta} {self.velocidad} {self.cilindrada}"

Andino=Coche("Rojo",4,4,"300 km/h","250cm")

print(Andino.descripcion())







        




    
    