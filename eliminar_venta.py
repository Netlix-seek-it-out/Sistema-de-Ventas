import json

def eliminar_venta(num_venta):
    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)


    compras["Ventas_registradas"] = [
        venta for venta in compras["Ventas_registradas"]
        if venta["num_venta"] != num_venta
    ]

    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2)