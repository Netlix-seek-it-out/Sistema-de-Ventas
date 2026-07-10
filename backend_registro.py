import json
from tkinter import messagebox 
from datetime import datetime
import os


def guardar_ventas(venta):  

    # Ruta para que funcione en un fork :D
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_actual, "registro.json") 

    with open(ruta_json, "r", encoding="utf-8") as bd:       
        compras = json.load(bd)



    # CREANDO EL NUMERO ID AUTOMATIZADO
    #Aseguradno que sea un numeor unico. Guardo el ultmio id recolectado, para que así, se evite numeros repetidos


    # COnvertir las cosas a minuscula

    producto_yay = venta["producto"].capitalize()
    cliente_yay= venta["cliente"].capitalize()

    venta["producto"] = producto_yay
    venta["cliente"] = cliente_yay

    numero_id = compras["ultimo_id_para_sumar"] + 1
    compras["ultimo_id_para_sumar"] = numero_id
    venta["num_venta"] = numero_id


    #AGREGANDO LA VEMTA AL JSON
    compras["Ventas_registradas"].append(venta)

    #Numero de venta mostrar
    messagebox.showinfo("N de venta", f"Total: {venta["total"]}, Numero de venta: {numero_id}")

    venta["fecha"] = datetime.now().strftime("%Y-%m-%d")

# Modifica el json, lo reescribe
    with open(ruta_json, "w", encoding="utf-8") as bd:
        json.dump(compras, bd, indent=2) 

