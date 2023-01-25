def aniobisiesto(anio):
    if anio%4==0 and anio%100!=0:
        return("el año es bisiesto")
    else:
        return("el año no es bisiesto")
    
print(aniobisiesto(1992))
print("hola mundo")    
