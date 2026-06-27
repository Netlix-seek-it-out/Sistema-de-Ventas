import json



def guardar_ventas(venta):    
    with open("registro.json", "r", encoding="utf-8") as bd:       
        compras = json.load(bd)

    compras["Ventas_registradas"].append(venta)


    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2) 
