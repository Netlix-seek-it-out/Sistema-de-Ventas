import tkinter as tk

import backend_registro as br

from calcular_estadisticas import calcular_estadisticas

from cargar_historial import cargar_historial

from realizar_busqueda import busqueda

from edicion_venta import editar_venta

#Esto lo cree para utilizar el canvas para la barra de busqueda, rendondear las esquinas
def crear_rect_redondeado(canvas, x1, y1, x2, y2, radio=18, **kwargs):
    puntos = [
        x1+radio, y1, x2-radio, y1, x2, y1, x2, y1+radio,
        x2, y2-radio, x2, y2, x2-radio, y2, x1+radio, y2,
        x1, y2, x1, y2-radio, x1, y1+radio, x1, y1
    ]
    return canvas.create_polygon(puntos, smooth=True, **kwargs)

def mostrar_estadisticas():
    edicion_frame.pack_forget()
    home_frame.pack_forget()
    registro_frame.pack_forget()
    historial_frame.pack_forget()


    #Pasarle el valor de ,las estadisticas y luego agregarlo al texto
    estadisticas = calcular_estadisticas()
    texto_ventana2.config(text=estadisticas["Total_ventas"])
    texto_clientes2.config(text=estadisticas["Cliente_lead"])
    texto_producto2.config(text=estadisticas["Mayor_producto"])
    texto_vingresos2.config(text= f"${estadisticas["Total_ingresos"]:.2f}")

    # Borramos las barras viejas para redibujarlas
    for widget in grafica_frame.winfo_children():
        if widget != grafica:
            widget.destroy()

    # Agarramos los datos reales
    dias = list(estadisticas["Ventas_por_dia"].items())
    max_val = max(v for _, v in dias) or 1

    # Dibujamos una barra por cada día
    for dia, val in dias:
        fila = tk.Frame(grafica_frame, bg="#2a2a3e")
        fila.pack(fill="x", padx=20, pady=3)
        tk.Label(fila, text=dia, font=("Segoe UI", 11), bg="#2a2a3e", fg="#9090b0", width=4, anchor="e").pack(side="left")
        barras = "█" * int((val / max_val) * 30)
        tk.Label(fila, text=f" {barras}", font=("Segoe UI", 11), bg="#2a2a3e", fg="#1D4ED8").pack(side="left")


    estadisticas_frame.pack(fill="both", expand=True)



def mostrar_home():
    estadisticas_frame.pack_forget()
    registro_frame.pack_forget()
    historial_frame.pack_forget()
    edicion_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)


def mostrar_registro():
    estadisticas_frame.pack_forget()
    home_frame.pack_forget()
    historial_frame.pack_forget()
    lbl_status.config(text="")
    limpiar_campos_registro()
    edicion_frame.pack_forget()
    registro_frame.pack(fill="both", expand=True)

def mostrar_historial():
    estadisticas_frame.pack_forget()
    home_frame.pack_forget()
    registro_frame.pack_forget()
    edicion_frame.pack_forget()
    cargar_historial(card, mostrar_edicion)
    historial_frame.pack(fill="both", expand=True)

def mostrar_edicion(venta=None):
    estadisticas_frame.pack_forget()
    home_frame.pack_forget()
    historial_frame.pack_forget()
    registro_frame.pack_forget()
    limpiar_campos_edicion()

    global venta_en_edicion
    venta_en_edicion = None


    if venta:

        venta_en_edicion = venta["num_venta"]
        # llenar edicion_entries con los datos de venta
        entries_edicion["cliente"].insert(0, venta["cliente"])
        # repetir con producto, cantidad, precio

        entries_edicion["producto"].insert(0, venta["producto"])


        entries_edicion["cantidad"].insert(0, venta["cantidad"])

    
        entries_edicion["precio"].insert(0, venta["precio"])
    edicion_frame.pack(fill="both", expand=True)

def ejecutar_busqueda():
    busqueda(buscar_barra, card, mostrar_edicion, historial_canvas)
    historial_canvas.update_idletasks()
    historial_canvas.configure(scrollregion=historial_canvas.bbox("all"))
    historial_canvas.yview_moveto(0)

screen = tk.Tk()

logo_original = tk.PhotoImage(file="ventacore (2).gif")
logo = logo_original.subsample(14, 14)

def agregar_logo(parent, fila, columna):
    canvas = tk.Canvas(
        parent,
        width=70,
        height=70,
        bg="#07142B",
        highlightthickness=0
    )

    canvas.grid(row=fila, column=columna, padx=12, pady=2)

    canvas.create_image(35, 35, image=logo)

    canvas.image = logo

screen.title("HOME")

screen.geometry("1200x600")
screen.state("zoomed")
screen.resizable(True, True)
screen.config(bg="#020B18")

home_frame = tk.Frame(screen
                       , bg="#000B22")
home_frame.pack(fill="both", expand=True)


#BARRA DE NAVEGACION
# Barra superior
nav_frame = tk.Frame(home_frame, bg="#07142B")
nav_frame.pack(fill="x", pady=(0, 0), ipady=1, ipadx=10)

menu_frame = tk.Frame(nav_frame, bg="#07142B")
menu_frame.pack(anchor="center", expand=True)


menu_frame.columnconfigure(4, weight=1)


agregar_logo(menu_frame, 0, 0)

# columnconfigure funciona así: el primer parametro es el índice en donde se encuentra la columna,
# y la segunda opción, el weight, es el peso o la importancia que tiene.

nombre_app = tk.Label(
    menu_frame,
    text="VentasCore",
    bg="#07142B",
    fg="#FFFFFF",
    width=12,
    height=1,
    font=("Segoe UI", 20, "bold"),
    cursor="hand2"
)
nombre_app.grid(row=0, column=1, padx=10, pady=8)

home_boton = tk.Label(
    menu_frame,
    text="🏠 HOME",
    bg="#07142B",
    fg="#19C8FF",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
home_boton.grid(row=0, column=2, padx=10, pady=0)

linea_home = tk.Frame(
    menu_frame,
    bg="#19C8FF",
    height=3,
    width=120
)

linea_home.grid(
    row=1,
    column=2,
    pady=(0, 5)
)

home_boton.bind("<Button-1>", lambda e: mostrar_home())

registro_boton_barra = tk.Label(
    menu_frame,
    text="📝 Registro",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    cursor="hand2",
    fg="#D8E3F3"
)
registro_boton_barra.grid(row=0, column=3, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())

estadisticas_boton_barra = tk.Label(
    menu_frame,
    text="📊 Estadisticas",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    cursor="hand2",
    fg="#D8E3F3"
)
estadisticas_boton_barra.grid(row=0, column=4, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(
    menu_frame,
    text="📄 Historial",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    cursor="hand2",
    fg="#D8E3F3"
)
historial_boton_barra.grid(row=0, column=5, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())



#FIN DE BARRA DE NAVEGACION


welcome_label = tk.Label(
    home_frame,
    text="VentasCore",
    bg="#000B22",
    fg="#00D4FF",
    font=("Segoe UI", 40, "bold")
)
welcome_label.pack(pady=(55, 5))

subtitle_label = tk.Label(
    home_frame,
    text="Sistema de gestión de ventas",
    bg="#000B22",
    fg="#A8B8D8",
    font=("Segoe UI", 15)
)
subtitle_label.pack(pady=(0, 35))

espacio = tk.Label(
    home_frame,
    bg="#0F1C34",
    height=1
)
espacio.pack(fill="x", pady=(0, 40))

binvenida_label = tk.Label(
    home_frame,
    text="¿Listo para comenzar?",
    bg="#000B22",
    fg="#F8FAFC",
    font=("Segoe UI", 20, "bold")
)
binvenida_label.pack(pady=(5, 10))


botones_frame = tk.Frame(home_frame,bg="#000B22")
botones_frame.pack(pady=(15, 35))

#NO se usan pack y grid juntos een un mismo elemento. Escoje uno, a mi daba errorj

registro_boton = tk.Label(
    botones_frame,
    text="🛒  Registrar Venta",
    bg="#1D4ED8",
    fg="#FFFFFF",
    font=("Segoe UI", 13, "bold"),
    cursor="hand2",
    width=24,
    height=2,
    bd=0,
    relief="flat"
)



#Funcion para que al pasar el mouse por encima del boton, cambie de color, y al salir vuelva a su color 
def entrar_mouse(e):
    registro_boton.config(bg="#1D4ED8")  # color más oscuro
 
def salir_mouse(e):
    registro_boton.config(bg="#2563EB")  # color original

registro_boton.bind("<Enter>", entrar_mouse)
registro_boton.bind("<Leave>", salir_mouse)



registro_boton.grid(row=0, column=0, padx=40, pady=5)
registro_boton.bind("<Button-1>", lambda e: mostrar_registro())


#.bind sirve para ejecutr un comando, casi igual que "button". 
# "button-1 es el indicador que dice que se realizara cuando se presione click derecho"

#LINK

buscar_boton_act = tk.Label(
    home_frame,
    text="Controla tus ventas de forma rápida y sencilla",
    bg="#000B22",
    fg="#94A3B8",
    font=("Segoe UI", 20),
    height=2
)
buscar_boton_act.pack(pady=(5, 0))



## ESTADISTICAS

estadisticas_frame = tk.Frame(screen, bg="#000B22")


#BARRA DE NAVEGACION
nav_frame = tk.Frame(estadisticas_frame, bg="#07142B")
nav_frame.pack(fill="x", pady=(0, 0), ipady=0, ipadx=10)


menu_frame = tk.Frame(nav_frame, bg="#07142B")
menu_frame.pack(anchor="center", expand=True)
menu_frame.columnconfigure(4, weight=1)

agregar_logo(menu_frame, 0, 0)

nombre_app = tk.Label(
    menu_frame,
    text="VentasCore",
    bg="#07142B",
    fg="#FFFFFF",
    width=12,
    height=1,
    font=("Segoe UI", 20, "bold"),
    cursor="hand2"
)
nombre_app.grid(row=0, column=1, padx=10, pady=8)

home_boton = tk.Label(
    menu_frame,
    text="🏠 HOME",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
home_boton.grid(row=0, column=2, padx=10, pady=0)
home_boton.bind("<Button-1>", lambda e: mostrar_home())

registro_boton_barra = tk.Label(
    menu_frame,
    text="📝 Registro",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    cursor="hand2"
)
registro_boton_barra.grid(row=0, column=3, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())

estadisticas_boton_barra = tk.Label(
    menu_frame,
    text="📊 Estadisticas",
    bg="#07142B",
    fg="#19C8FF",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    cursor="hand2"
)
estadisticas_boton_barra.grid(row=0, column=4, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

linea_estadisticas = tk.Frame(
    menu_frame,
    bg="#19C8FF",
    height=3,
    width=120
)
linea_estadisticas.grid(
    row=1,
    column=4,
    pady=(0, 5)
)

historial_boton_barra = tk.Label(
    menu_frame,
    text="📄 Historial",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=2,
    font=("Arial", 12, "bold"),
    cursor="hand2"
)
historial_boton_barra.grid(row=0, column=5, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())
# Fin de la barra 

titulo = tk.Label(estadisticas_frame, text="📊 Estadísticas", font=("Segoe UI", 35, "bold"), bg="#000B22", fg="#19C8FF")
titulo.pack(pady=(30, 15))

cuadros = tk.Frame(estadisticas_frame, bg="#000B22")
cuadros.pack()

fila1 = tk.Frame(cuadros, bg="#000B22")
fila1.pack(pady=15)



ventas = tk.Frame(fila1, bg="#0F1C34", width=220, height=150)
ventas.pack(side="left", padx=15)
ventas.pack_propagate(False)
texto_ventana1=tk.Label(ventas, text="🛒", font=("Segoe UI", 22,"bold"), bg="#0F1C34", fg="#19C8FF").pack(pady=(18, 2))
texto_ventana2=tk.Label(ventas, text="0", font=("Segoe UI", 15, "bold"), bg="#0F1C34", fg="#FFFFFF")
texto_ventana2.pack()
texto_ventana3=tk.Label(ventas, text="Total de ventas", font=("Segoe UI", 11,"bold"), bg="#0F1C34", fg="#9FB6D9").pack()

        
producto = tk.Frame(fila1, bg="#0F1C34", width=220, height=150)
producto.pack(side="left", padx=15)
producto.pack_propagate(False)
texto_producto1=tk.Label(producto, text="🏆", font=("Segoe UI", 22,"bold"), bg="#0F1C34", fg="#19C8FF").pack(pady=(18, 2))
texto_producto2=tk.Label(producto, text="Lacto", font=("Segoe UI", 15, "bold"), bg="#0F1C34", fg="white")
texto_producto2.pack()
texto_producto3=tk.Label(producto, text="Producto más vendido", font=("Segoe UI", 11,"bold"), bg="#0F1C34", fg="#9FB6D9", wraplength=180).pack()


cliente = tk.Frame(fila1, bg="#0F1C34", width=220, height=150)
cliente.pack(side="left", padx=15)
cliente.pack_propagate(False)
texto_clientes1=tk.Label(cliente, text="👤", font=("Segoe UI", 22,"bold"), bg="#0F1C34", fg="#19C8FF").pack(pady=(18, 2))
texto_clientes2=tk.Label(cliente, text="Nehemias", font=("Segoe UI", 15, "bold"), bg="#0F1C34", fg="white")
texto_clientes2.pack()
texto_clientes3=tk.Label(cliente, text="Mejor cliente", font=("Segoe UI", 11,"bold"), bg="#0F1C34", fg="#9FB6D9").pack()


ingresos = tk.Frame(fila1, bg="#0F1C34", width=220, height=150)
ingresos.pack(side="left", padx=15)
ingresos.pack_propagate(False)
texto_vingresos1=tk.Label(ingresos, text="💰", font=("Segoe UI", 22,"bold"), bg="#0F1C34", fg="#19C8FF").pack(pady=(18, 2))
texto_vingresos2=tk.Label(ingresos, text="$500", font=("Segoe UI", 15, "bold"), bg="#0F1C34", fg="white")
texto_vingresos2.pack()
texto_vingresos3=tk.Label(ingresos, text="Total de ingresos", font=("Segoe UI", 11,"bold"), bg="#0F1C34", fg="#9FB6D9").pack()



grafica_frame = tk.Frame(estadisticas_frame, bg="#0F1C34", highlightbackground="#19C8FF", highlightthickness=2)
grafica_frame.pack(padx=40, pady=15, fill="both", expand=True)

grafica = tk.Label(grafica_frame, text="📊 Gráfica de ventas",font=("Segoe UI", 14,"bold"), bg="#0F1C34", fg="#19C8FF")
grafica.pack(anchor="w", padx=20, pady=(15, 10))


nombre_app.grid(row=0, column=1)
home_boton.grid(row=0, column=2)
registro_boton_barra.grid(row=0, column=3)
estadisticas_boton_barra.grid(row=0, column=4)
historial_boton_barra.grid(row=0, column=5)


# REGISTRO DE VENTAS ___ FRAME DE VENTANA

registro_frame = tk.Frame(screen, bg="#000B22")

#BARRA DE NAVEGACION
nav_frame = tk.Frame(registro_frame, bg="#07142B")
nav_frame.pack(fill="x", pady=(0, 0), ipady=(0), ipadx=10)

menu_frame = tk.Frame(nav_frame, bg="#07142B")
menu_frame.pack(anchor="center", expand=True)

menu_frame.columnconfigure(4, weight=1)


agregar_logo(menu_frame, 0, 0)

nombre_app = tk.Label(
    menu_frame,
    text="VentasCore",
    bg="#07142B",
    width=12,
    height=1,
    font=("Arial", 20, "bold"),
    fg="#FFFFFF",
    cursor="hand2"
)
nombre_app.grid(row=0, column=1, padx=10, pady=8)

home_boton = tk.Label(
    menu_frame,
    text="🏠 HOME",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
home_boton.grid(row=0, column=2, padx=10, pady=0)
home_boton.bind("<Button-1>", lambda e: mostrar_home())

registro_boton_barra = tk.Label(
    menu_frame,
    text="📝 Registro",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    fg="#19C8FF",
    cursor="hand2"
)
registro_boton_barra.grid(row=0, column=3, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())

linea_registro = tk.Frame(
    menu_frame,
    bg="#19C8FF",
    width=120,
    height=3
)
linea_registro.grid(
    row=1,
    column=3,
    pady=(0, 5)
)

estadisticas_boton_barra = tk.Label(
    menu_frame,
    text="📊 Estadísticas",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
estadisticas_boton_barra.grid(row=0, column=4, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(
    menu_frame,
    text="📄 Historial",
    bg="#07142B",
    width=18,
    height=1,
    font=("Arial", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
historial_boton_barra.grid(row=0, column=5, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())

# Titulo
tk.Label(registro_frame, text="Registrar venta",
         bg="#000B22", fg="#19C8FF",
         font=("Segoe UI", 30 , "bold")).pack(pady=(40, 30))

# Campo con las 6 etiquetas
form_frame = tk.Frame(registro_frame, bg="#000B22")
form_frame.pack(padx=120, fill="x")

left_col = tk.Frame(form_frame, bg="#000B22")
left_col.pack(side="left", fill="both", expand=True, padx=(0, 40))

right_col = tk.Frame(form_frame, bg="#000B22")
right_col.pack(side="left", fill="both", expand=True, padx=(40, 0))

entries = {}

def validar_numero(valor):
    return valor == "" or valor.replace(".", "", 1).isdigit()

vcmd = (registro_frame.register(validar_numero), "%P")

def make_field(parent, key, label_text):
    tk.Label(parent, text=label_text, bg="#000B22",
             fg="#D8E3F3", font=("Segoe UI", 12, "bold")).pack(anchor="w")
    
    if key == "cantidad":
        entry = tk.Entry(
        parent,
        bg="#102445",
        fg="#D8E3F3",
        insertbackground="#19C8FF",
        relief="flat",
        font=("Segoe UI", 13),
        validate="key",
        validatecommand=vcmd
    )
    else:
        entry = tk.Entry(
        parent,
        bg="#102445",
        fg="#D8E3F3",
        insertbackground="#19C8FF",
        relief="flat",
        font=("Segoe UI", 13)
    )
    
    entry.pack(fill="x", pady=(4, 60), ipady=10)
    entries[key] = entry

# Columna izquierda
make_field(left_col,  "cliente",   "Nombre del cliente:")
make_field(left_col,  "cantidad",  "Cantidad de unidades:")

# Columna derecha
make_field(right_col, "producto",  "Producto vendido:")

tk.Label(right_col, text="Precio unitario:", bg="#000B22",
         fg="#ffffff", font=("Segoe UI", 12,"bold")).pack(anchor="w")

precio_frame = tk.Frame(right_col, bg="#102445")
precio_frame.pack(fill="x", pady=(4, 60))

tk.Label(precio_frame, text="$", bg="#102445", fg="#cdd6f4",
         font=("Segoe UI", 13)).pack(side="left", padx=(10, 0), ipady=10)

entry_precio = tk.Entry(
    precio_frame,
    bg="#102445",
    fg="#cdd6f4",
    insertbackground="#cdd6f4",
    relief="flat",
    font=("Segoe UI", 13),
    validate="key",
    validatecommand=vcmd
)
entry_precio.pack(side="left", fill="x", expand=True, ipady=10)

entries["precio"] = entry_precio


from tkinter import messagebox 
def limpiar_campos_registro():
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
        "cliente": entries["cliente"].get(),
        "producto": entries["producto"].get(),
        "cantidad": entries["cantidad"].get(),
        "precio": entries["precio"].get(),
    }


    #CALCULANDO EL TOTAL, Asegurandose que no sean numero negativos, y calculando el total
    try:
        
        cantifad_numerador = float(venta["cantidad"])
        precio_numerador = float(venta["precio"])

        if cantifad_numerador <= 0 or precio_numerador <= 0:
            messagebox.showerror("ERROR", "nesesitas ingresar un valor mayor que cero para poder registrar tu venta")
            return
        
        total = cantifad_numerador * precio_numerador
        venta["total"]  = total




    except ValueError:
        messagebox.showerror("ERROR", "ingrese datos válidos en la cantidad y precio")
        return

    br.guardar_ventas(venta)
    lbl_status.config(text="Venta guardada correctamente.")
    limpiar_campos_registro()


# Boton
btn = tk.Button(
    registro_frame,
    text="Guardar Venta",
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    font=("Segoe UI", 12, "bold"),
    padx=40,
    pady=12,
    command=guardar_datos_ventas
)
btn.pack(pady=35)
lbl_status = tk.Label(registro_frame, text="", bg="#1e1e2e",
                       fg="#a6e3a1", font=("Segoe UI", 11))
lbl_status.pack(pady=12)

def entrar_mouse(e):
    btn.config(bg="#1D4ED8")

def salir_mouse(e):
    btn.config(bg="#2563EB")

btn.bind("<Enter>", entrar_mouse)
btn.bind("<Leave>", salir_mouse)

nombre_app.grid(row=0, column=1)
home_boton.grid(row=0, column=2)
registro_boton_barra.grid(row=0, column=3)
estadisticas_boton_barra.grid(row=0, column=4)
historial_boton_barra.grid(row=0, column=5)


## HISTORIAL___FRAME___VENTANA
historial_frame = tk.Frame(screen, bg="#000B22")

# ===================== BARRA DE NAVEGACIÓN =====================

nav_frame = tk.Frame(historial_frame, bg="#07142B")
nav_frame.pack(fill="x", pady=(0, 0), ipady=0, ipadx=10)

menu_frame = tk.Frame(nav_frame, bg="#07142B")
menu_frame.pack(anchor="center", expand=True)

menu_frame.columnconfigure(4, weight=1)


agregar_logo(menu_frame, 0, 0)

nombre_app = tk.Label(
    menu_frame,
    text="VentasCore",
    bg="#07142B",
    fg="#FFFFFF",
    width=12,
    height=1,
    font=("Segoe UI", 20, "bold"),
    cursor="hand2"
)
nombre_app.grid(row=0, column=1, padx=10, pady=8)

home_boton = tk.Label(
    menu_frame,
    text="🏠 HOME",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
home_boton.grid(row=0, column=2, padx=10, pady=0)
home_boton.bind("<Button-1>", lambda e: mostrar_home())

registro_boton_barra = tk.Label(
    menu_frame,
    text="📝 Registro",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
registro_boton_barra.grid(row=0, column=3, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())

estadisticas_boton_barra = tk.Label(
    menu_frame,
    text="📊 Estadísticas",
    bg="#07142B",
    fg="#D8E3F3",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
estadisticas_boton_barra.grid(row=0, column=4, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())

historial_boton_barra = tk.Label(
    menu_frame,
    text="📄 Historial",
    bg="#07142B",
    fg="#19C8FF",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    cursor="hand2"
)
historial_boton_barra.grid(row=0, column=5, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())

linea_historial = tk.Frame(
    menu_frame,
    bg="#19C8FF",
    width=120,
    height=3
)

linea_historial.grid(
    row=1,
    column=5,
    pady=(0, 5)
)


# ===================== TÍTULO =====================

barra_ante_superior = tk.Frame(historial_frame, bg="#000B22")
barra_ante_superior.pack(anchor="w", pady=15)

tk.Label(
    barra_ante_superior,
    text="Historial",
    bg="#000B22",
    fg="#FFFFFF",
    font=("Segoe UI", 20, "bold")
).grid(row=0, column=0, padx=(30,50))

buscar_label = tk.Label(
    barra_ante_superior,
    text="Ingresar número de venta:",
    font=("Segoe UI",12,"bold"),
    fg="#D8E3F3",
    bg="#000B22"
)
buscar_label.grid(row=0, column=2, pady=5)

borde_buscar = tk.Frame(
    barra_ante_superior,
    bg="#1E4C8C",
    highlightthickness=1
)
borde_buscar.grid(row=0, column=3, padx=10, pady=5)

# ===================== BARRA DE BÚSQUEDA =====================

COLOR_NORMAL = "#1B4D8D"
COLOR_FOCUS  = "#19C8FF"

# Canvas del campo de búsqueda
buscar_canvas = tk.Canvas(
    barra_ante_superior,
    width=320,
    height=44,
    bg="#000B22",
    highlightthickness=0
)
buscar_canvas.grid(row=0, column=3, padx=10, pady=5)

# Rectángulo redondeado
rect_buscar = crear_rect_redondeado(
    buscar_canvas,
    2,
    2,
    318,
    42,
    radio=20,
    fill="#081B38",
    outline=COLOR_NORMAL,
    width=2
)

# Caja de texto
buscar_barra = tk.Entry(
    buscar_canvas,
    bg="#081B38",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    relief="flat",
    font=("Segoe UI", 12),
    bd=0
)

buscar_canvas.create_window(
    145,
    22,
    window=buscar_barra,
    width=250,
    height=28
)

# Lupa
buscar_canvas.create_text(
    295,
    22,
    text="🔍",
    fill="#19C8FF",
    font=("Segoe UI Emoji", 12)
)

def al_enfocar(e):
    buscar_canvas.itemconfig(
        rect_buscar,
        outline=COLOR_FOCUS,
        fill="#102C57"
    )

def al_desenfocar(e):
    buscar_canvas.itemconfig(
        rect_buscar,
        outline=COLOR_NORMAL,
        fill="#081B38"
    )

buscar_barra.bind("<FocusIn>", al_enfocar)
buscar_barra.bind("<FocusOut>", al_desenfocar)


# Contenedor que va a tener el Canvas + Scrollbar
scroll_container = tk.Frame(
    historial_frame,
    bg="#000B22"
)
scroll_container.pack(fill="both", expand=True, padx=20, pady=10)

# Canvas donde vive el scroll
historial_canvas = tk.Canvas(
    scroll_container,
    bg="#000B22",
    highlightthickness=0
)
historial_canvas.pack(side="left", fill="both", expand=True)

# Barra de scroll
historial_scrollbar = tk.Scrollbar(
    scroll_container,
    orient="vertical",
    bg="#07142B",
    troughcolor="#000B22",
    activebackground="#19C8FF",
    width=20,
    command=historial_canvas.yview
)
   

historial_scrollbar.pack(side="right", fill="y", padx=(5,5))
historial_canvas.configure(yscrollcommand=historial_scrollbar.set)

# Frame donde se dibujan las tarjetas
card = tk.Frame(
    historial_canvas,
    bg="#000B22"
)

historial_canvas.create_window(
    (0, 0),
    window=card,
    anchor="nw"
)

def actualizar_scroll_historial(event):
    historial_canvas.configure(
        scrollregion=historial_canvas.bbox("all")
    )

card.bind("<Configure>", actualizar_scroll_historial)

buscar_barra.bind(
    "<Return>",
    lambda e: ejecutar_busqueda()
)
## --- Botón de buscar ---

btn_buscar_canvas = tk.Canvas(
    barra_ante_superior,
    width=140,
    height=44,
    bg="#000B22",
    highlightthickness=0,
    cursor="hand2"
)

btn_buscar_canvas.grid(row=0, column=4, padx=10, pady=5)


btn_rect = crear_rect_redondeado(
    btn_buscar_canvas,
    2,
    2,
    138,
    42,
    radio=20,
    fill="#1E6BFF",
    outline=""
)

btn_texto = btn_buscar_canvas.create_text(
    70,
    22,
    text="Buscar",
    fill="#FFFFFF",
    font=("Segoe UI", 11, "bold")
)


def btn_hover(e):
    btn_buscar_canvas.itemconfig(
        btn_rect,
        fill="#19C8FF"
    )


def btn_salir(e):
    btn_buscar_canvas.itemconfig(
        btn_rect,
        fill="#1E6BFF"
    )


def btn_presionar(e):
    btn_buscar_canvas.itemconfig(
        btn_rect,
        fill="#1554C0"
    )


def btn_soltar(e):
    btn_buscar_canvas.itemconfig(
        btn_rect,
        fill="#19C8FF"
    )
    ejecutar_busqueda()


for item in (btn_rect, btn_texto):
    btn_buscar_canvas.tag_bind(item, "<Enter>", btn_hover)
    btn_buscar_canvas.tag_bind(item, "<Leave>", btn_salir)
    btn_buscar_canvas.tag_bind(item, "<ButtonPress-1>", btn_presionar)
    btn_buscar_canvas.tag_bind(item, "<ButtonRelease-1>", btn_soltar)


mensaje = tk.Label(
    card,
    text="Tus registros",
    bg="#000B22",
    fg="#FFFFFF",
    font=("Segoe UI", 11, "bold")
)

mensaje.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

nombre_app.grid(row=0, column=1)
home_boton.grid(row=0, column=2)
registro_boton_barra.grid(row=0, column=3)
estadisticas_boton_barra.grid(row=0, column=4)
historial_boton_barra.grid(row=0, column=5)


### EDICION FRAME

edicion_frame = tk.Frame(screen, bg="#000B22")

# BARRA DE NAVEGACION
nav_frame = tk.Frame(edicion_frame, bg="#07142B")
nav_frame.pack(fill="x", pady=(0, 0), ipady=0, ipadx=10)


menu_frame = tk.Frame(nav_frame, bg="#07142B")
menu_frame.pack(anchor="center", expand=True)

menu_frame.columnconfigure(4, weight=1)

agregar_logo(menu_frame, 0, 0)

nombre_app = tk.Label(
    menu_frame,
    text="VentasCore",
    bg="#07142B",
    width=12,
    height=1,
    font=("Segoe UI", 20, "bold"),
    fg="#FFFFFF",
    cursor="hand2"
)
nombre_app.grid(row=0, column=1, padx=10, pady=8)


home_boton = tk.Label(
    menu_frame,
    text="🏠 HOME",
    bg="#07142B",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
home_boton.grid(row=0, column=2, padx=10, pady=0)
home_boton.bind("<Button-1>", lambda e: mostrar_home())


registro_boton_barra = tk.Label(
    menu_frame,
    text="📝 Registro",
    bg="#07142B",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
registro_boton_barra.grid(row=0, column=3, padx=10, pady=8)
registro_boton_barra.bind("<Button-1>", lambda e: mostrar_registro())


estadisticas_boton_barra = tk.Label(
    menu_frame,
    text="📊 Estadísticas",
    bg="#07142B",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    fg="#D8E3F3",
    cursor="hand2"
)
estadisticas_boton_barra.grid(row=0, column=4, padx=10, pady=8)
estadisticas_boton_barra.bind("<Button-1>", lambda e: mostrar_estadisticas())


historial_boton_barra = tk.Label(
    menu_frame,
    text="📄 Historial",
    bg="#07142B",
    width=18,
    height=1,
    font=("Segoe UI", 12, "bold"),
    fg="#19C8FF",
    cursor="hand2"
)
historial_boton_barra.grid(row=0, column=5, padx=10, pady=8)
historial_boton_barra.bind("<Button-1>", lambda e: mostrar_historial())


# Línea activa debajo de Historial
linea_activa = tk.Frame(
    menu_frame,
    bg="#19C8FF",
    height=3,
    width=120
)

linea_activa.grid(
    row=1,
    column=5,
    pady=(0, 3)
)


# Titulo
tk.Label(edicion_frame, text="Editar venta",
         bg="#000B22", fg="#FFFFFF",
         font=("Segoe UI", 30, "bold")).pack(pady=(40, 30))

# Campo con las 6 etiquetas
form_frame = tk.Frame(edicion_frame, bg="#000B22")
form_frame.pack(padx=120, fill="x")

left_col = tk.Frame(form_frame, bg="#000B22")
left_col.pack(side="left", fill="both", expand=True, padx=(0, 40))

right_col = tk.Frame(form_frame, bg="#000B22")
right_col.pack(side="left", fill="both", expand=True, padx=(40, 0))

entries_edicion = {}

def make_field(parent, key, label_text):
    tk.Label(
    parent,
    text=label_text,
    bg="#000B22",
    fg="#D8E3F3",
    font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0,5))


    entry = tk.Entry(parent, bg="#07142B", fg="#FFFFFF",
                     insertbackground="#FFFFFF", relief="flat",
                     font=("Segoe UI", 13))
    
    entry.pack(fill="x", pady=(4, 60), ipady=10, ipadx=20)
    entries_edicion[key] = entry

# Columna izquierda
make_field(left_col,  "cliente",   "Nombre del cliente:")
make_field(left_col,  "cantidad",  "Cantidad de unidades:")

# Columna derecha
make_field(right_col, "producto",  "Producto vendido:")

tk.Label(
    right_col,
    text="Precio unitario:",
    bg="#000B22",
    fg="#D8E3F3",
    font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0,5))

precio_frame = tk.Frame(right_col, bg="#07142B")
precio_frame.pack(fill="x", pady=(4, 60))

tk.Label(precio_frame, text="$", bg="#07142B", fg="#D8E3F3",
         font=("Segoe UI", 13)).pack(side="left", padx=(10, 0), ipady=10)

entry_precio = tk.Entry(precio_frame, bg="#07142B", fg="#FFFFFF",
                        insertbackground="#FFFFFF", relief="flat",
                        font=("Segoe UI", 13))

entry_precio.pack(side="left", fill="x", expand=True, ipady=10)

entries_edicion["precio"] = entry_precio

nombre_app.grid(row=0, column=1)
home_boton.grid(row=0, column=2)
registro_boton_barra.grid(row=0, column=3)
estadisticas_boton_barra.grid(row=0, column=4)
historial_boton_barra.grid(row=0, column=5)

from tkinter import messagebox

def limpiar_campos_edicion():
   for campo in entries_edicion.values():
       campo.delete(0, tk.END)

def editar():
    
    if venta_en_edicion is None:
        messagebox.showerror("ERROR", "No hay venta seleccionada para editar.")
        return

    for key in ["cliente", "producto", "cantidad", "precio"]:
        if entries_edicion[key].get().strip() == "":
            messagebox.showwarning(
                "Registro incompleto",
                "Completa todos los campos antes de guardar." )
            return 

   
    venta = {
        "cliente": entries_edicion["cliente"].get(),
        "producto": entries_edicion["producto"].get(),
        "cantidad": entries_edicion["cantidad"].get(),
        "precio": entries_edicion["precio"].get(),
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

    editar_venta(venta_en_edicion, venta)
    limpiar_campos_edicion()
    lbl_status.config(text="Venta guardada correctamente.")

# Boton
btn = tk.Button(edicion_frame, text="Guardar Venta",
                bg="#7c6af7", fg="#ffffff",
                activebackground="#9a8cff", activeforeground="#ffffff",
                relief="flat", font=("Segoe UI", 13, "bold"),
                cursor="hand2", command=editar)
btn.pack(ipadx=40, ipady=12, pady=(20, 0))

lbl_status = tk.Label(edicion_frame, text="", bg="#000B22",
                       fg="#a6e3a1", font=("Segoe UI", 11))
lbl_status.pack(pady=12)

def entrar_mouse(e):
    btn.config(bg="#5a4bd6")

def salir_mouse(e):
    btn.config(bg="#7c6af7")

btn.bind("<Enter>", entrar_mouse)
btn.bind("<Leave>", salir_mouse)

screen.mainloop()