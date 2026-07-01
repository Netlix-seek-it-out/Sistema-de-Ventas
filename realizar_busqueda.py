import json
from tkinter import messagebox

def busqueda(valor_buscar):
    try:
        valor = int(valor_buscar.get())
        
    except ValueError:
        messagebox.showerror("ERROR", "ingrese el numero de venta")
    