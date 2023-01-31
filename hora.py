import datetime

hora_actual = datetime.datetime.now()

if hora_actual.hour < 19:
    print("Todavia se puede jugar")
else:
    print("es hora de volver a casa")
