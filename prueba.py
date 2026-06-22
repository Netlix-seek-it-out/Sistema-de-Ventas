import json

with open("prueba.json", "r", encoding="utf-8") as db:
    datos = json.load(db)

#LEER DATOS
print(datos)

#Agregar algo nuevo
datos["estudiantes"][0]["bachillerato"] = "Tecpan"

#
datos["estudiantes"][1]["bachillerato"] = "ninguno"


#datos["estudiantes"][0].pop("ERROR")

with open("prueba.json", "w", encoding="utf-8") as db:
    json.dump(datos, db, indent=2)