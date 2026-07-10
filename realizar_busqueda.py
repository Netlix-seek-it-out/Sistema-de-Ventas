import json
from tkinter import messagebox
import tkinter as tk
from eliminar_venta import eliminar_venta
import os
#from cargar_historial import cargar_historial





def busqueda(valor_buscar, padre, abrir_edicion, historial_canvas):

    try:
        valor = int(valor_buscar.get())
        
    except ValueError:
        messagebox.showerror("ERROR", "ingrese el numero de venta")
    
    # 1. Obtenemos el texto que el usuario escribió
    texto = valor_buscar.get().strip()

    if texto == "":
        messagebox.showwarning("Aviso", "Escribe un número de venta para buscar.")
        return

    # 2. Validamos que sea un número
    try:
        num_buscado = int(texto)
    except ValueError:
        messagebox.showerror("ERROR", "Ingresa solo el número de venta (ejemplo: 5)")
        return
        ## Ruta para que funcione en un fork :D
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(carpeta_actual, "registro.json") 

    with open(ruta_json, "r", encoding="utf-8") as bd:
        compras = json.load(bd)

    # 4. Buscamos la venta con ese número
    encontrada = None
    for venta in compras["Ventas_registradas"]:
        if venta["num_venta"] == num_buscado:
            encontrada = venta
            break

    # 5. Limpiamos lo que había antes en el frame (la lista completa del historial)
    for widget in padre.winfo_children():
        widget.destroy()

    # 6. Si no encontramos nada, avisamos
    if encontrada is None:
        tk.Label(padre, text=f"❌ No se encontró la venta #{num_buscado}",
                 bg="#2a2a3e", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
        return

    # 7. Si sí la encontramos, la mostramos igual que en el historial
    venta_frame = tk.Frame(padre, bg="#313145")
    venta_frame.pack(fill="x", pady=20, padx=22, ipadx=8, ipady=5)

    datos_frame = tk.Frame(venta_frame, bg="#313145")
    datos_frame.pack(side="left", fill="x", expand=True)

    tk.Label(datos_frame, text=f"📦 Venta #{encontrada['num_venta']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"👤 Cliente: {encontrada['cliente']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"📦 Producto: {encontrada['producto']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"🔢 Cantidad: {encontrada['cantidad']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"💲 Precio: ${encontrada['precio']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"🟰 Total: ${encontrada['total']}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)
    tk.Label(datos_frame, text=f"📅 Fecha: {encontrada.get('fecha', 'Sin fecha')}", bg="#313145", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", pady=5, padx=10)


    acciones_frame = tk.Frame(venta_frame, bg="#313145")
    acciones_frame.pack(side="right", padx=20)

    tk.Button(acciones_frame, text="Editar",
            command=lambda venta=encontrada: abrir_edicion(venta),
        bg="#1D4ED8", width=10, height=2, font=("arial", 10, "bold"), fg="#fbfbfb", 
        cursor="hand2").pack(pady=15, padx=10)

## Funcion parab eliminar el resultado yey

    def eliminar_resultado():
        eliminar_venta(encontrada["num_venta"])

        for widget in padre.winfo_children():
            widget.destroy()
        tk.Label(padre, text="Venta eliminada").pack()

    tk.Button(
            acciones_frame, 
            text="Eliminar", 
            bg="#F74B01", 
            width=10, 
            height=2, 
            font=("arial", 10, "bold"), 
            fg="#fbfbfb", 
            cursor="hand2", 
            command=eliminar_resultado).pack(pady=15, padx=10)

