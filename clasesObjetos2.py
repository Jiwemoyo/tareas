class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def resultado(self):
        if self.nota>6:
            print(f"el alumno {self.nombre} a aprovado con una nota de {self.nota}")
        else:
            print(f"el alumno {self.nombre} a reprovado con una nota de {self.nota}")
            


alumno1 = Alumno("Alessandro",7)

alumno1.resultado() 

