import tkinter as tk

screen = tk.Tk()

screen.title("HOME")

screen.geometry("1000x600")
screen.resizable(True, True)
screen.config(bg="#1e1e2e")

padre_frame = tk.Frame(screen
                       , bg="#1e1e2e")
padre_frame.pack(pady=0, padx=0, fill=("both"))

#BARRA DE NAVEGACION
# Barra superior
nav_frame = tk.Frame(padre_frame, bg="#1e293b")
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

#barra_navegacion = tk.Frame(padre_frame, bg="#154162", padx=15, pady=15)
#barra_navegacion.pack(pady=10)
#registrar_venta_barra = tk.Label(barra_navegacion, text="Registrar ventas", bg="#001A2E", font=("arial", 14), fg="darkblue")
#registrar_venta_barra.grid(row=0, column=0, padx=2, pady=2)

#FIN DE BARRA DE NAVEGACION

welcome_label = tk.Label(padre_frame, text="¡Bienvenido a Indago!", bg="#1e1e2e", font=("Arial", 20, "bold"), fg="#f8fafc")
welcome_label.pack(pady=(60, 20))

espacio = tk.Label(padre_frame, bg="#161a22")
espacio.pack(pady=10, fill="x")

binvenida_label = tk.Label(padre_frame, text="¿Que quieres hacer?", font=("arial",20,"bold italic"), fg="#cdd6f4", bg="#1e1e2e")
binvenida_label.pack(pady=30)


botones_frame = tk.Frame(padre_frame, bg="#1e1e2e", pady=20, padx=20)
botones_frame.pack(pady=20)

#NO se usan pack y grid juntos een un mismo elemento. Escoje uno, a mi daba errorj

registro_boton = tk.Label(botones_frame, text="Registar venta ✏️", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7",
     width=18, height=2)
#registro_boton.bind("<Button-1>", lambda e: funcion)
registro_boton.grid(row=0, column=0, padx=40, pady=10)
#.bind sirve para ejecutr un comando, casi igual que "button". 
# "button-1 es el indicador que dice que se realizara cuando se presione click derecho"

historial_boton = tk.Label(botones_frame, text="Ver Historial 📄", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7", 
    width=18, height=2)
historial_boton.grid(row=0, column=1, padx=40, pady=10)
# LINK

estadisticas_boton = tk.Label(botones_frame, text="Estadisticas 📊", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7", width=18, height=2)
estadisticas_boton.grid(row=0, column=2, padx=40, pady=10)


buscar_label = tk.Label(padre_frame, text="Buscar...", font=("arial", 12, "bold"), fg="#cdd6f4", bg="#1e1e2e")
buscar_label.pack(pady=10)


borde_buscar = tk.Frame(padre_frame, bg="#5596ff", highlightthickness=1)
borde_buscar.pack(pady=5, padx=10)

buscar_barra = tk.Entry(borde_buscar, bg="#313145", width=25, font=("arial", 16), fg="#fbfbfb")
buscar_barra.pack(pady=1, ipady=5)

screen.mainloop()