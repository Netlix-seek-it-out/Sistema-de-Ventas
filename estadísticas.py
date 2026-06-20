
import tkinter as tk

ventana = tk.Tk()
ventana.title("resumen de ventana ")
ventana.geometry("900x650")
ventana.config(bg="#1e1e2e")

titulo = tk.Label(ventana,text="📊 Estadisticas",font=("Segoe UI",24,"bold"),bg="#1e1e2e",fg="#8B5CF6")
titulo.pack(pady=40)


contenedor = tk.Frame(ventana, bg="#1e1e2e")
contenedor.pack(expand=True)



fila1 = tk.Frame(contenedor, bg="#1e1e2e")
fila1.pack(pady=50)

tarjetas_1 = tk.Frame(fila1, bg="#7A68EE", width=280, height=160)
tarjetas_1.pack(side="left", padx=80)
tarjetas_1.pack_propagate(False)
tex_targeta1 = tk.Label(tarjetas_1, text="🛒 Total de ventas", font=("Segoe UI",16,"bold"), bg="#7A68EE", fg="#ffffff")
tex_targeta1.pack(expand=True)

tarjetas_2 = tk.Frame(fila1, bg="#7A68EE", width=280, height=160)
tarjetas_2.pack(side="left", padx=80)
tarjetas_2.pack_propagate(False)
tex_targeta2 = tk.Label(tarjetas_2, text="🏆 Producto más vendido", font=("Segoe UI",16,"bold"), bg="#7A68EE", fg="#ffffff")
tex_targeta2.pack(expand=True)


fila2 = tk.Frame(contenedor, bg="#1e1e2e")
fila2.pack(pady=30)

tarjetas_3 = tk.Frame(fila2, bg="#7A68EE", width=280, height=160)
tarjetas_3.pack(side="left", padx=80)
tarjetas_3.pack_propagate(False)
tex_targeta3 = tk.Label(tarjetas_3, text="👤Mejor cliente ", font=("Segoe UI",16,"bold"), bg="#7A68EE", fg="#ffffff")
tex_targeta3.pack(expand=True)

tarjetas_4 = tk.Frame(fila2, bg="#7A68EE", width=280, height=160)
tarjetas_4.pack(side="left", padx=80)
tarjetas_4.pack_propagate(False)
tex_targeta4 = tk.Label(tarjetas_4, text="💰 Total de Ingresos ", font=("Segoe UI",16,"bold"), bg="#7A68EE", fg="#ffffff")
tex_targeta4.pack(expand=True)

ventana.mainloop()