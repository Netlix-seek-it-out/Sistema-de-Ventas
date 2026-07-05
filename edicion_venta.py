import json

def editar_venta(num_venta, venta_actualizada):
    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)

    for venta in compras["Ventas_registradas"]:
        if venta["num_venta"] == num_venta:
            venta["cliente"] = venta_actualizada["cliente"]
            venta["producto"] = venta_actualizada["producto"]
            venta["cantidad"] = venta_actualizada["cantidad"]
            venta["precio"] = venta_actualizada["precio"]
            venta["total"] = venta_actualizada["total"]
            break
        
    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2)