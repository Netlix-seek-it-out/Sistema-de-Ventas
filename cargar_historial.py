import json
import tkinter as tk

def cargar_historial(padre):

    #carta = tk.Frame(padre, bg="#2a2a3e")

    for widget in padre.winfo_children():
        widget.destroy()

    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)
    
    ventas_diccionario = compras["Ventas_registradas"]

    for venta in ventas_diccionario:
        venta_frame = tk.Frame(padre, bg="#313145")
        venta_frame.pack(fill="x", pady=8, padx=18)

        tk.Label(venta_frame, text=f"Venta #{venta['num_venta']}", bg="#313145", fg="white").pack(anchor="w")
        tk.Label(venta_frame, text=f"Cliente: {venta['cliente']}", bg="#313145", fg="white").pack(anchor="w")
        tk.Label(venta_frame, text=f"Producto: {venta['producto']}", bg="#313145", fg="white").pack(anchor="w")
        tk.Label(venta_frame, text=f"Cantidad: {venta['cantidad']}", bg="#313145", fg="white").pack(anchor="w")
        tk.Label(venta_frame, text=f"Precio: ${venta['precio']}", bg="#313145", fg="white").pack(anchor="w")
        tk.Label(venta_frame, text=f"Total: ${venta['total']}", bg="#313145", fg="white").pack(anchor="w")