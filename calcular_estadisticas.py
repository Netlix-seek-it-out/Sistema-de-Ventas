import json

#venta = {"elemento 1": "valor", "Ventas_registradas": [
#    {
#        "Nombre": "Nahomy"
#    },
#    {
#        "Nombre": "May"
#    }
#    ]}

def calcular_estadisticas():    
    with open("registro.json", "r", encoding="utf-8") as bd:       
        compras = json.load(bd)


    total_ventas = len(compras["Ventas_registradas"])
    return total_ventas

#print(calcular_estadisticas(venta))

