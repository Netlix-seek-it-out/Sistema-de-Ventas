import json
from tkinter import messagebox

def put_num_venta(compras):
    return len(compras["Ventas_registradas"]) + 1

def guardar_ventas(venta):    
    with open("registro.json", "r", encoding="utf-8") as bd:       
        compras = json.load(bd)


    # CREANDO EL NUMERO ID AUTOMATIZADO
    #numero_id = put_num_venta(compras)
    #venta["num_venta"] = numero_id

    #AGREGANDO LA VEMTA AL JSON
    compras["Ventas_registradas"].append(venta)

# Modifica el json, lo reescribe
    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2) 

