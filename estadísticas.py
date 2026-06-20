
import tkinter as tk

ventana = tk.Tk()
ventana.title("Estadísticas de Ventas")
ventana.geometry("1000x700")
ventana.config(bg="#1e1e2e")

titulo = tk.Label(ventana, text="📊 Estadísticas", font=("Segoe UI", 35, "bold"), bg="#1e1e2e", fg="#8B5CF6")
titulo.pack(pady=(30, 15))

cuadros = tk.Frame(ventana, bg="#1e1e2e")
cuadros.pack()

fila1 = tk.Frame(cuadros, bg="#1e1e2e")
fila1.pack(pady=15)


ventas = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
ventas.pack(side="left", padx=15)
ventas.pack_propagate(False)
texto_ventana1=tk.Label(ventas, text="🛒", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_ventana2=tk.Label(ventas, text="0", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white").pack()
texto_ventana3=tk.Label(ventas, text="Total de ventas", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()

 
producto = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
producto.pack(side="left", padx=15)
producto.pack_propagate(False)
texto_producto1=tk.Label(producto, text="🏆", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_producto2=tk.Label(producto, text="Lacto", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white").pack()
texto_producto3=tk.Label(producto, text="Producto más vendido", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff", wraplength=180).pack()


cliente = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
cliente.pack(side="left", padx=15)
cliente.pack_propagate(False)
texto_clientes1=tk.Label(cliente, text="👤", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_clientes2=tk.Label(cliente, text="Nehemias", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white").pack()
texto_clientes3=tk.Label(cliente, text="Mejor cliente", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()


ingresos = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
ingresos.pack(side="left", padx=15)
ingresos.pack_propagate(False)
texto_vingresos1=tk.Label(ingresos, text="💰", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_vingresos2=tk.Label(ingresos, text="$500", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white").pack()
texto_vingresos3=tk.Label(ingresos, text="Total de ingresos", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()



grafica_frame = tk.Frame(ventana, bg="#2a2a3e", highlightbackground="#7A68EE", highlightthickness=2)
grafica_frame.pack(padx=40, pady=15, fill="both", expand=True)

grafica = tk.Label(grafica_frame, text="📊 Gráfica de ventas",font=("Segoe UI", 14, "bold"), bg="#2a2a3e", fg="#8B5CF6")
grafica.pack(anchor="w", padx=20, pady=(15, 10))

dias = [("Lun", 2), ("Mar", 5), ("Mié", 4), ("Jue", 7), ("Vie", 6), ("Sáb", 3), ("Dom", 1)]

max_val = max(v for _, v in dias)

for dia, val in dias:
    fila = tk.Frame(grafica_frame, bg="#2a2a3e")
    fila.pack(fill="x", padx=20, pady=3)

    tk.Label(fila, text=dia, font=("Segoe UI", 11),bg="#2a2a3e", fg="#9090b0", width=4,anchor="e").pack(side="left")

    barras = "█" * int((val / max_val) * 30)
    tk.Label(fila, text=f" {barras}",font=("Segoe UI", 11),bg="#2a2a3e", fg="#7A68EE").pack(side="left")

ventana.mainloop()