import json

def editar_venta(num_venta):
    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)




    with open("registro.json", "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2)