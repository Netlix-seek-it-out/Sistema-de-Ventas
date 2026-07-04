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


# Titulo
barra_ante_superior = tk.Frame(historial_frame, bg="#1e1e2e")
barra_ante_superior.pack(anchor="w", pady=10)


tk.Label(barra_ante_superior, text="Historial", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, padx=(30, 50), pady=(5, 5))

espacio = tk.Label(barra_ante_superior, bg="#1e1e2e", width=6)
espacio.grid(pady=10, padx=6, row=0, column=1)

buscar_label = tk.Label(barra_ante_superior, text="Ingresar número de venta:", font=("arial", 12, "bold"), fg="#cdd6f4", bg="#1e1e2e")
buscar_label.grid(pady=5, row=0, column=2)


borde_buscar = tk.Frame(barra_ante_superior, bg="#313145", highlightthickness=1)
borde_buscar.grid(pady=5, padx=10, row=0, column=3)

#Barra de busqueda

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

# boton de buscar

btn_buscar_canvas = tk.Canvas(barra_ante_superior, width=140, height=44,
                               bg="#1e1e2e", highlightthickness=0, cursor="hand2")
btn_buscar_canvas.grid(row=0, column=4, padx=10, pady=5)

btn_rect = crear_rect_redondeado(btn_buscar_canvas, 2, 2, 138, 42, radio=20,
                                  fill="#7A68EE", outline="")
btn_texto = btn_buscar_canvas.create_text(70, 22, text=" Buscar",
                                           fill="white", font=("Segoe UI", 11, "bold"))

# Lupa a la derecha
buscar_canvas.create_text(
    295, 22,              
    text="🔍",
    fill="#bdbdd7",
    font=("Segoe UI Emoji", 12)
)

# Entry 
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



mensaje = tk.Label(
    card,
    text="Tus registros",
    bg="#2a2a3e",
    fg="white",
    font=("Arial", 11, "bold")
)
mensaje.place(relx=0.5, rely=0.5,
              anchor="center")


screen.mainloop() 