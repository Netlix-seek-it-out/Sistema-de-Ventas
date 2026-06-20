
import tkinter as tk

ventana = tk.Tk()
ventana.title("resumen de ventana ")
ventana.geometry("900x650")
ventana.config(bg="#1e1e2e")

nav_frame = tk.Frame(ventana, bg="#1e293b")
nav_frame.columnconfigure(3, weight=1)
nav_frame.pack(fill="x", expand=True, pady=(0, 10), ipady=(3), ipadx=10)

menu_frame = tk.Frame(nav_frame, bg="#1e293b")
menu_frame.pack(anchor="center", expand=True)


#columnconfigure funciona así: el primer parametro es el indie en donde se encuentra la columna, y la segunda opcion, el weight, es el peso, o la importancia que tiene, si tiene weight=1, el widget cubrirá todo el espacio sobrante. Si uuno tiene un weight de 2, cubrirá más espacio del sobrante.
# rowconfigure funciona igual pero para las filas

nombre_app = tk.Label(menu_frame,  text="¡Indago!", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#f8fafc")
nombre_app.grid(row=0, column=0)

 
registro_boton_barra = tk.Label(
    menu_frame, text="📝 Registro", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2",
      fg="#94a3b8")
registro_boton_barra.grid(row=0, column=1, padx=10, pady=8)


estadisticas_boton_barra = tk.Label(menu_frame, text="📊 Estadisticas", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
estadisticas_boton_barra.grid(row=0, column=2, padx=10, pady=8)

historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
historial_boton_barra.grid(row=0, column=3, padx=10, pady=8)


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