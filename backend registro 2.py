from HOME import *
from tkinter import messagebox



def venta(precio, cantidad):
        
        
    

    if(precio <= -0):
        messagebox.showinfo("ERROR", "nesesitas ingresar un valor mayor que cero para poder registrar tu venta")
    elif(cantidad <= 0):
        messagebox.showinfo("ERROR", "nesesitas ingresar una cantidad mayor que cero para poder guardar la venta")