import datetime

hora_actual = datetime.datetime.now()

if hora_actual.hour > 19:
    print("es hora de ir a casa")
else:
    salida= 17 - hora_actual.hour 
    print(f"faltan {salida} para irse a casa")
