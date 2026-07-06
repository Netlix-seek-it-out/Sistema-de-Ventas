import json
from tkinter import messagebox

def busqueda(valor_buscar):
    try:
        valor = int(valor_buscar.get())
        
    except ValueError:
        messagebox.showerror("ERROR", "ingrese el numero de venta")
    
    import json
import tkinter as tk
from tkinter import messagebox

def busqueda(valor_buscar, padre):
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

    # 3. Leemos el archivo con todas las ventas
    with open("registro.json", "r", encoding="utf-8") as bd:
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
    venta_frame.pack(fill="x", pady=8, padx=18)
