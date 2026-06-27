import json

def put_num_venta(compras):
    return len(compras["Ventas_registradas"]) + 1

#venta = {"w": "g"}

def guardar_ventas(venta):    
    with open("registro.json", "r", encoding="utf-8") as bd:       
        compras = json.load(bd)

    numero_id = put_num_venta(compras)
    venta["num_venta"] = numero_id
    compras["Ventas_registradas"].append(venta)





    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2) 

    return numero_id

#print(guardar_ventas(venta))
