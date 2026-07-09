import json
import os

def eliminar_venta(num_venta):
    ## Ruta para que funcione en un fork :D
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_actual, "registro.json")

    with open(ruta_json, "r", encoding="utf-8") as bd:
        compras = json.load(bd)


    compras["Ventas_registradas"] = [
        venta for venta in compras["Ventas_registradas"]
        if venta["num_venta"] != num_venta
    ]

    with open(ruta_json, "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2)