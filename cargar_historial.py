import json
import tkinter as tk
from eliminar_venta import eliminar_venta

def cargar_historial(padre, abrir_edicion):



    for widget in padre.winfo_children():
        widget.destroy()

    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)
    
    ventas_diccionario = compras["Ventas_registradas"]

    for venta in ventas_diccionario:
        venta_frame = tk.Frame(padre, bg="#07142B")
        venta_frame.pack(fill="x", pady=8, padx=18)


        datos_frame = tk.Frame(venta_frame, bg="#07142B")
        datos_frame.pack(side="left", fill="x", expand=True)

        acciones_frame = tk.Frame(venta_frame, bg="#07142B")
        acciones_frame.pack(side="right", padx=20)

        tk.Label(datos_frame, text=f"📦 Venta #{venta['num_venta']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"👤 Cliente: {venta['cliente']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"📦 Producto: {venta['producto']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"🔢 Cantidad: {venta['cantidad']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"💲 Precio: ${venta['precio']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"🟰 Total: ${venta['total']}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")
        tk.Label(datos_frame, text=f"📅 Fecha: {venta.get('fecha', 'Sin fecha')}", bg="#07142B", fg="#19C8FF", font=("Arial", 10, "bold")).pack(anchor="w")

        tk.Button(acciones_frame, text="Editar",
            command=lambda venta=venta: abrir_edicion(venta),

            bg="#1E40AF", width=10, height=2, font=("arial", 10, "bold"), fg="#FFFFFF", 
            cursor="hand2").pack(pady=5, padx=10)

        #id = venta["num_venta"]
        tk.Button(
            acciones_frame, 
            text="Eliminar", 
            bg="#991B1B", 
            width=10, 
            height=2, 
            font=("arial", 10, "bold"), 
            fg="#fbfbfb", 
            cursor="hand2", 
            command=lambda num_venta=venta["num_venta"]: (eliminar_venta(num_venta), cargar_historial(padre, abrir_edicion,))).pack(pady=5, padx=10)

