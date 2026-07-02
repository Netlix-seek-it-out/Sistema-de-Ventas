import tkinter as tk

import backend_registro as br

from calcular_estadisticas import calcular_estadisticas

from cargar_historial import cargar_historial

from realizar_busqueda import busqueda

def crear_rect_redondeado(canvas, x1, y1, x2, y2, radio=18, **kwargs):
    puntos = [
        x1+radio, y1, x2-radio, y1, x2, y1, x2, y1+radio,
        x2, y2-radio, x2, y2, x2-radio, y2, x1+radio, y2,
        x1, y2, x1, y2-radio, x1, y1+radio, x1, y1
    ]
    return canvas.create_polygon(puntos, smooth=True, **kwargs)

def mostrar_estadisticas():
    home_frame.pack_forget()
    registro_frame.pack_forget()
    historial_frame.pack_forget()


    #Pasarle el valor de ,as estadisticas y luego agregarlo al texto
    estadisticas = calcular_estadisticas()
    texto_ventana2.config(text=estadisticas["Total_ventas"])
    texto_clientes2.config(text=estadisticas["Cliente_lead"])
    texto_producto2.config(text=estadisticas["Mayor_producto"])
    texto_vingresos2.config(text= f"${estadisticas["Total_ingresos"]:.2f}")


    estadisticas_frame.pack(fill="both", expand=True)



def mostrar_home():
    estadisticas_frame.pack_forget()
    registro_frame.pack_forget()
    historial_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)


def mostrar_registro():
    estadisticas_frame.pack_forget()
    home_frame.pack_forget()
    historial_frame.pack_forget()
    lbl_status.config(text="")
    limpiar_campos()
    registro_frame.pack(fill="both", expand=True)

def mostrar_historial():
    estadisticas_frame.pack_forget()
    home_frame.pack_forget()
    registro_frame.pack_forget()
    cargar_historial(card)
    historial_frame.pack(fill="both", expand=True)



screen = tk.Tk()

screen.title("HOME")

screen.geometry("1200x600")
screen.resizable(True, True)
screen.config(bg="#1e1e2e")

home_frame = tk.Frame(screen
                       , bg="#1e1e2e")
home_frame.pack(fill="both", expand=True)

#BARRA DE NAVEGACION
# Barra superior
nav_frame = tk.Frame(home_frame, bg="#1e293b")
nav_frame.pack(fill="x", pady=(0, 0), ipady=3, ipadx=10)

menu_frame = tk.Frame(nav_frame, bg="#1e293b")
menu_frame.pack(anchor="center", expand=True)


menu_frame.columnconfigure(4, weight=1)


#columnconfigure funciona así: el primer parametro es el indie en donde se encuentra la columna, y la segunda opcion, el weight, es el peso, o la importancia que tiene, si tiene weight=1, el widget cubrirá todo el espacio sobrante. Si uuno tiene un weight de 2, cubrirá más espacio del sobrante.
# rowconfigure funciona igual pero para las filas


nombre_app = tk.Label(menu_frame,  text="¡Indago!", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#7A68EE", cursor="hand2")
nombre_app.grid(row=0, column=0, padx=10, pady=8)

home_boton = tk.Label(menu_frame,  text="HOME", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#E2DEEA", cursor="hand2")
home_boton.grid(row=0, column=1, padx=10, pady=8)

registro_boton_barra = tk.Label(
    menu_frame, text="📝 Registro", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2",
      fg="#94a3b8")
registro_boton_barra.grid(row=0, column=2, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())


estadisticas_boton_barra = tk.Label(menu_frame, text="📊 Estadisticas", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
estadisticas_boton_barra.grid(row=0, column=3, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
historial_boton_barra.grid(row=0, column=4, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())


#FIN DE BARRA DE NAVEGACION

welcome_label = tk.Label(home_frame, text="¡Bienvenido a Indago!", bg="#1e1e2e", font=("Arial", 20, "bold"), fg="#f8fafc")
welcome_label.pack(pady=(60, 20))

espacio = tk.Label(home_frame, bg="#161a22")
espacio.pack(pady=10, fill="x")

binvenida_label = tk.Label(home_frame, text="¿Que quieres hacer?", font=("arial",20,"bold italic"), fg="#cdd6f4", bg="#1e1e2e")
binvenida_label.pack(pady=30)


botones_frame = tk.Frame(home_frame, bg="#1e1e2e", pady=20, padx=20)
botones_frame.pack(pady=20)

#NO se usan pack y grid juntos een un mismo elemento. Escoje uno, a mi daba errorj

registro_boton = tk.Label(botones_frame, text="Registar venta ✏️", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7",
     width=18, height=2)
registro_boton.grid(row=0, column=0, padx=40, pady=10)
registro_boton.bind("<Button-1>", lambda e: mostrar_registro())

#.bind sirve para ejecutr un comando, casi igual que "button". 
# "button-1 es el indicador que dice que se realizara cuando se presione click derecho"

# LINK

estadisticas_boton = tk.Label(botones_frame, text="Estadisticas 📊", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7", width=18, height=2)
estadisticas_boton.grid(row=0, column=1, padx=40, pady=10)
estadisticas_boton.bind("<Button-1>", lambda e: mostrar_estadisticas())
#"<button-1>" representa exactamente el click izquierdo

historial_boton = tk.Label(botones_frame, text="Ver Historial 📄", font=("arial", 12, "bold"), fg="#cdd6f4", cursor="hand2", bg="#7c6af7", 
    width=18, height=2)
historial_boton.grid(row=0, column=2, padx=40, pady=10)
historial_boton.bind("<Button-1>", lambda e: mostrar_historial())

#buscar_label = tk.Label(home_frame, text="Buscar...", font=("arial", 12, "bold"), fg="#cdd6f4", bg="#1e1e2e")
#buscar_label.pack(pady=5)


#borde_buscar = tk.Frame(home_frame, bg="#5596ff", highlightthickness=1)
#borde_buscar.pack(pady=5, padx=10)

#buscar_barra = tk.Entry(borde_buscar, bg="#313145", width=25, font=("arial", 16), fg="#fbfbfb")
#buscar_barra.pack(pady=1, ipady=5)

buscar_boton_act = tk.Label(home_frame, text="¡Mantén tus compras organizadas!", font=("arial", 18, "bold"), fg="#e4e4e4", cursor="hand2", bg="#1e1e2e", 
    height=3)
buscar_boton_act.pack(pady=20)



## ESTADISTICAS

estadisticas_frame = tk.Frame(screen, bg="#1e1e2e")


#BARRA DE NAVEGACION
nav_frame = tk.Frame(estadisticas_frame, bg="#1e293b")
nav_frame.pack(fill="x", pady=(0, 0), ipady=3, ipadx=10)


menu_frame = tk.Frame(nav_frame, bg="#1e293b")
menu_frame.pack(anchor="center", expand=True)
menu_frame.columnconfigure(4, weight=1)


nombre_app = tk.Label(menu_frame,  text="¡Indago!", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#7A68EE", cursor="hand2")
nombre_app.grid(row=0, column=0, padx=10, pady=8)

home_boton = tk.Label(menu_frame,  text="HOME", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#E2DEEA", cursor="hand2")
home_boton.grid(row=0, column=1, padx=10, pady=8)
home_boton.bind("<Button-1>", lambda e: mostrar_home())
   
registro_boton_barra = tk.Label(
            menu_frame, text="📝 Registro", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2",
            fg="#94a3b8")
registro_boton_barra.grid(row=0, column=2, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())


estadisticas_boton_barra = tk.Label(menu_frame, text="📊 Estadisticas", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
estadisticas_boton_barra.grid(row=0, column=3, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: None)

historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
historial_boton_barra.grid(row=0, column=4, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())




titulo = tk.Label(estadisticas_frame, text="📊 Estadísticas", font=("Segoe UI", 35, "bold"), bg="#1e1e2e", fg="#8B5CF6")
titulo.pack(pady=(30, 15))

cuadros = tk.Frame(estadisticas_frame, bg="#1e1e2e")
cuadros.pack()

fila1 = tk.Frame(cuadros, bg="#1e1e2e")
fila1.pack(pady=15)



ventas = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
ventas.pack(side="left", padx=15)
ventas.pack_propagate(False)
texto_ventana1=tk.Label(ventas, text="🛒", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_ventana2=tk.Label(ventas, text="0", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white")
texto_ventana2.pack()
texto_ventana3=tk.Label(ventas, text="Total de ventas", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()

        
producto = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
producto.pack(side="left", padx=15)
producto.pack_propagate(False)
texto_producto1=tk.Label(producto, text="🏆", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_producto2=tk.Label(producto, text="Lacto", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white")
texto_producto2.pack()
texto_producto3=tk.Label(producto, text="Producto más vendido", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff", wraplength=180).pack()


cliente = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
cliente.pack(side="left", padx=15)
cliente.pack_propagate(False)
texto_clientes1=tk.Label(cliente, text="👤", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_clientes2=tk.Label(cliente, text="Nehemias", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white")
texto_clientes2.pack()
texto_clientes3=tk.Label(cliente, text="Mejor cliente", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()


ingresos = tk.Frame(fila1, bg="#7A68EE", width=220, height=150)
ingresos.pack(side="left", padx=15)
ingresos.pack_propagate(False)
texto_vingresos1=tk.Label(ingresos, text="💰", font=("Segoe UI", 22,"bold"), bg="#7A68EE", fg="white").pack(pady=(18, 2))
texto_vingresos2=tk.Label(ingresos, text="$500", font=("Segoe UI", 20, "bold"), bg="#7A68EE", fg="white")
texto_vingresos2.pack()
texto_vingresos3=tk.Label(ingresos, text="Total de ingresos", font=("Segoe UI", 11,"bold"), bg="#7A68EE", fg="#d0c8ff").pack()



grafica_frame = tk.Frame(estadisticas_frame, bg="#2a2a3e", highlightbackground="#7A68EE", highlightthickness=2)
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




# REGISTRO DE VENTAS ___ FRAME DE VENTANA

registro_frame = tk.Frame(screen, bg="#1e1e2e")

#BARRA DE NAVEGACION
nav_frame = tk.Frame(registro_frame, bg="#1e293b")
nav_frame.pack(fill="x", pady=(0, 10), ipady=(3), ipadx=10)

menu_frame.columnconfigure(4, weight=1)

menu_frame = tk.Frame(nav_frame, bg="#1e293b")
menu_frame.pack(anchor="center", expand=True)


nombre_app = tk.Label(menu_frame,  text="¡Indago!", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#7A68EE", cursor="hand2")
nombre_app.grid(row=0, column=0, padx=10, pady=8)

home_boton = tk.Label(menu_frame,  text="HOME", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#E2DEEA", cursor="hand2")
home_boton.grid(row=0, column=1, padx=10, pady=8)
home_boton.bind("<Button-1>", lambda e: mostrar_home())
    

    
registro_boton_barra = tk.Label(
            menu_frame, text="📝 Registro", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2",
            fg="#94a3b8")
registro_boton_barra.grid(row=0, column=2, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())



estadisticas_boton_barra = tk.Label(menu_frame, text="📊 Estadisticas", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
estadisticas_boton_barra.grid(row=0, column=3, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
historial_boton_barra.grid(row=0, column=4, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())


# Titulo
tk.Label(registro_frame, text="Registrar venta",
         bg="#1e1e2e", fg="#cdd6f4",
         font=("Segoe UI", 20, "bold")).pack(pady=(40, 30))

# Campo con las 6 etiquetas
form_frame = tk.Frame(registro_frame, bg="#1e1e2e")
form_frame.pack(padx=120, fill="x")

left_col = tk.Frame(form_frame, bg="#1e1e2e")
left_col.pack(side="left", fill="both", expand=True, padx=(0, 40))

right_col = tk.Frame(form_frame, bg="#1e1e2e")
right_col.pack(side="left", fill="both", expand=True, padx=(40, 0))

entries = {}

def make_field(parent, key, label_text):
    tk.Label(parent, text=label_text, bg="#1e1e2e",
             fg="#a6adc8", font=("Segoe UI", 12)).pack(anchor="w")
    entry = tk.Entry(parent, bg="#313145", fg="#cdd6f4",
                     insertbackground="#cdd6f4", relief="flat",
                     font=("Segoe UI", 13))
    entry.pack(fill="x", pady=(4, 60), ipady=10)
    entries[key] = entry

# Columna izquierda
#make_field(left_col,  "num_venta", "Numero de venta:")
make_field(left_col,  "cliente",   "Nombre del cliente:")
make_field(left_col,  "cantidad",  "Cantidad de unidades:")

# Columna derecha
make_field(right_col, "producto",  "Producto vendido:")
make_field(right_col, "precio",    "Precio unitario:")
#make_field(right_col, "total",     "Total:")

from tkinter import messagebox 
def limpiar_campos():
   for campo in entries.values():
       campo.delete(0, tk.END)

def guardar_datos_ventas():
    
    

    for key in ["cliente", "producto", "cantidad", "precio"]:
        if entries[key].get().strip() == "":
            messagebox.showwarning(
                "Registro incompleto",
                "Completa todos los campos antes de guardar." )
            return 

   
    venta = {
        #"num_venta": entries["num_venta"].get(),
        "cliente": entries["cliente"].get(),
        "producto": entries["producto"].get(),
        "cantidad": entries["cantidad"].get(),
        "precio": entries["precio"].get(),
        #"total": entries["total"].get()
    }


    #CALCULANDO EL TOTAL, Asegurandose que no sean numero negativos, y calculando el total
    try:
        
        cantifad_numerador = float(venta["cantidad"])
        precio_numerador = float(venta["precio"])

        if cantifad_numerador <= 0 or precio_numerador <= 0:
            messagebox.showerror("ERROR", "nesesitas ingresar un valor mayor que cero para poder registrar tu venta")
            return
        
        total = cantifad_numerador * precio_numerador
        messagebox.showinfo("TOTAL DE VENTA", f"Total: {total}")
        venta["total"]  = total


    except ValueError:
        messagebox.showerror("ERROR", "ingrese datos válidos en la cantidad y precio")
        return

    br.guardar_ventas(venta)
    limpiar_campos()
    lbl_status.config(text="Venta guardada correctamente.")

# Boton
btn = tk.Button(registro_frame, text="Guardar Venta",
                bg="#7c6af7", fg="#ffffff",
                activebackground="#9a8cff", activeforeground="#ffffff",
                relief="flat", font=("Segoe UI", 13, "bold"),
                cursor="hand2", command=guardar_datos_ventas)
btn.pack(ipadx=40, ipady=12, pady=(20, 0))

lbl_status = tk.Label(registro_frame, text="", bg="#1e1e2e",
                       fg="#a6e3a1", font=("Segoe UI", 11))
lbl_status.pack(pady=12)






## HSITORIAL___FRAME___VENTANA

historial_frame = tk.Frame(screen, bg="#1e1e2e")

nav_frame = tk.Frame(historial_frame, bg="#1e293b")
nav_frame.pack(fill="x", pady=(0, 0), ipady=(3), ipadx=10)


menu_frame.columnconfigure(4, weight=1)

menu_frame = tk.Frame(nav_frame, bg="#1e293b")
menu_frame.pack(anchor="center", expand=True)

nombre_app = tk.Label(menu_frame,  text="¡Indago!", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#7A68EE", cursor="hand2")
nombre_app.grid(row=0, column=0, padx=10, pady=8)

home_boton = tk.Label(menu_frame,  text="HOME", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), fg="#E2DEEA", cursor="hand2")
home_boton.grid(row=0, column=1, padx=10, pady=8)
home_boton.bind("<Button-1>", lambda e: mostrar_home())
    

 
registro_boton_barra = tk.Label(
    menu_frame, text="📝 Registro", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2",
      fg="#94a3b8")
registro_boton_barra.grid(row=0, column=2, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())


estadisticas_boton_barra = tk.Label(menu_frame, text="📊 Estadisticas", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
estadisticas_boton_barra.grid(row=0, column=3, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
historial_boton_barra.grid(row=0, column=4, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())

# barra del naveagdors
#nav = tk.Frame(historial_frame, bg="#252535", height=40)
#nav.pack(fill="x")
#tk.Label(nav, text="¡Indago!", bg="#252535", fg="#7b6cf6", font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=8)

# Titulo
barra_ante_superior = tk.Frame(historial_frame, bg="#1e1e2e")
barra_ante_superior.pack(anchor="w", pady=10)


tk.Label(barra_ante_superior, text="Historial", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=(30, 50), pady=(5, 5))

espacio = tk.Label(barra_ante_superior, bg="#1e1e2e", width=6)
espacio.grid(pady=10, padx=6, row=0, column=1)

buscar_label = tk.Label(barra_ante_superior, text="Ingrese numero de venta", font=("arial", 12, "bold"), fg="#cdd6f4", bg="#1e1e2e")
buscar_label.grid(pady=5, row=0, column=2)


borde_buscar = tk.Frame(barra_ante_superior, bg="#313145", highlightthickness=1)
borde_buscar.grid(pady=5, padx=10, row=0, column=3)

# --- BARRA DE BÚSQUEDA CON BORDES REDONDEADOS ---

COLOR_NORMAL = "#3a3a55"
COLOR_FOCUS  = "#7A68EE"

buscar_canvas = tk.Canvas(barra_ante_superior, width=320, height=44,
                           bg="#1e1e2e", highlightthickness=0)
buscar_canvas.grid(row=0, column=3, padx=10, pady=5)

rect_buscar = crear_rect_redondeado(
    buscar_canvas, 2, 2, 318, 42, radio=20,
    fill="#252538", outline=COLOR_NORMAL, width=2
)

buscar_barra = tk.Entry(buscar_canvas, bg="#252538", fg="#fbfbfb",
                         insertbackground="#fbfbfb", relief="flat",
                         font=("Segoe UI", 12), bd=0)
buscar_canvas.create_window(160, 22, window=buscar_barra, width=280, height=28)

def al_enfocar(e):
    buscar_canvas.itemconfig(rect_buscar, outline=COLOR_FOCUS, fill="#2c2c44")

def al_desenfocar(e):
    buscar_canvas.itemconfig(rect_buscar, outline=COLOR_NORMAL, fill="#252538")

buscar_barra.bind("<FocusIn>", al_enfocar)
buscar_barra.bind("<FocusOut>", al_desenfocar)
buscar_barra.bind("<Return>", lambda e: busqueda(buscar_barra))

# --- BOTÓN DE BUSCAR CON BORDES REDONDEADOS ---

btn_buscar_canvas = tk.Canvas(barra_ante_superior, width=140, height=44,
                               bg="#1e1e2e", highlightthickness=0, cursor="hand2")
btn_buscar_canvas.grid(row=0, column=4, padx=10, pady=5)

btn_rect = crear_rect_redondeado(btn_buscar_canvas, 2, 2, 138, 42, radio=20,
                                  fill="#7A68EE", outline="")
btn_texto = btn_buscar_canvas.create_text(70, 22, text=" Buscar",
                                           fill="white", font=("Segoe UI", 11, "bold"))

# Lupa a la derecha
buscar_canvas.create_text(
    295, 22,              # Cerca del borde derecho
    text="🔍",
    fill="#bdbdd7",
    font=("Segoe UI Emoji", 12)
)

# Entry un poco más angosto para dejar espacio a la lupa
buscar_canvas.create_window(
    145, 22,
    window=buscar_barra,
    width=250,
    height=28
)
def btn_hover(e):
    btn_buscar_canvas.itemconfig(btn_rect, fill="#9a8cff")

def btn_salir(e):
    btn_buscar_canvas.itemconfig(btn_rect, fill="#7A68EE")

def btn_presionar(e):
    btn_buscar_canvas.itemconfig(btn_rect, fill="#5a4bd6")

def btn_soltar(e):
    btn_buscar_canvas.itemconfig(btn_rect, fill="#9a8cff")
    busqueda(buscar_barra)

for item in (btn_rect, btn_texto):
    btn_buscar_canvas.tag_bind(item, "<Enter>", btn_hover)
    btn_buscar_canvas.tag_bind(item, "<Leave>", btn_salir)
    btn_buscar_canvas.tag_bind(item, "<ButtonPress-1>", btn_presionar)
    btn_buscar_canvas.tag_bind(item, "<ButtonRelease-1>", btn_soltar)




# Tarjeta
card = tk.Frame(historial_frame, bg="#2a2a3e")
card.pack(fill="both", expand=True, padx=20, pady=5)
#for item in ["Registro", "Estadísticas", "Historial"]:
#    tk.Label(nav, text=item, bg="#252535", fg="#a0a0c0", font=("Arial", 9)).pack(side="left", padx=10)


mensaje = tk.Label(
    card,
    text="Tus registros",
    bg="#2a2a3e",
    fg="white",
    font=("Arial", 11, "bold")
)
mensaje.place(relx=0.5, rely=0.5,
              anchor="center")

#dias= ["lunes:","martes:","miercoles:","jueves:","viernes:","sabado:","domingo:"]

#for dia in dias:
#    tk.Label(card, text=dia, bg="#2a2a3e", fg="white", font=("Arial", 12,)).pack(anchor="w", padx=20, pady=2)

# Resumen
#tk.Label(card, text="Resumen", bg="#2a2a3e", fg="white", font=("Arial", 11, "bold")).pack(anchor="w", padx=15, pady=(10, 2))




screen.mainloop()