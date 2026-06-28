import json

with open ("base_datos.json","r",encoding="utf-8") as bd:
    compras =json.load (bd)  

def guardar_ventas():
    num_venta =()