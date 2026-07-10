import json
import os

def editar_venta(num_venta, venta_actualizada):
    ## Ruta para que funcione en un fork :D
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_actual, "registro.json")

    with open(ruta_json, "r", encoding="utf-8") as bd:
        compras = json.load(bd)

    for venta in compras["Ventas_registradas"]:
        if venta["num_venta"] == num_venta:
            venta["cliente"] = venta_actualizada["cliente"]
            venta["producto"] = venta_actualizada["producto"]
            venta["cantidad"] = venta_actualizada["cantidad"]
            venta["precio"] = venta_actualizada["precio"]
            venta["total"] = venta_actualizada["total"]
            break
        
    with open(ruta_json, "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2)