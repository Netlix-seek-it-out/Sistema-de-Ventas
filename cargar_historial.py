import json
import tkinter as tk
from eliminar_venta import eliminar_venta
import os





def cargar_historial(padre, abrir_edicion):

    for widget in padre.winfo_children():
        widget.destroy()

        
## Ruta para que funcione en un fork :D
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_actual, "registro.json")
    
    with open(ruta_json, "r", encoding="utf-8") as bd:
        compras = json.load(bd)
   
    ventas_diccionario = compras["Ventas_registradas"]

    #Columnas 3 jejeje
    columnas = 3

    ## Configurando la forma y el espacio que abracara cada columna

    for col in range(3):
        padre.grid_columnconfigure(col, weight=1)

    for i, venta in enumerate(ventas_diccionario):

        fila = i // columnas
        columna_sola = i % columnas

        venta_frame = tk.Frame(padre, bg="#313145")
        venta_frame.grid(row=fila, column=columna_sola, pady=20, padx=22, ipadx=8, ipady=5, sticky="nsew")

        datos_frame = tk.Frame(venta_frame, bg="#313145")
        datos_frame.pack(side="left", fill="x", expand=True)


        acciones_frame = tk.Frame(venta_frame, bg="#313145")
        acciones_frame.pack(side="right", padx=20)


        tk.Label(datos_frame, text=f"📦 Venta #{venta['num_venta']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"👤 Cliente: {venta['cliente']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"📦 Producto: {venta['producto']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"🔢 Cantidad: {venta['cantidad']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"💲 Precio: ${venta['precio']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"🟰 Total: ${venta['total']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)
        tk.Label(datos_frame, text=f"📅 Fecha: {venta.get('fecha', 'Sin fecha')}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=4, padx=10)

        tk.Button(acciones_frame, text="Editar",
            command=lambda venta=venta: abrir_edicion(venta),


            bg="#1D4ED8", width=10, height=2, font=("arial", 10, "bold"), fg="#fbfbfb",
            cursor="hand2").pack(pady=15, padx=(10, 0))

        #id = venta["num_venta"]
        tk.Button(
            acciones_frame,
            text="Eliminar",
            bg="#F74B01",
            width=10,
            height=2,
            font=("arial", 10, "bold"),
            fg="#fbfbfb",
            cursor="hand2",
            command=lambda num_venta=venta["num_venta"]: (eliminar_venta(num_venta), cargar_historial(padre, abrir_edicion,))).pack(pady=15, padx=(10, 0))


