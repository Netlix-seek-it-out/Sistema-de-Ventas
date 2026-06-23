import tkinter as tk


def abrir_estadisticas(ventana_home):
        ventana_home.destroy()

        ventana = tk.Tk()
        #tk.Toplevel crea una ventana hija que aparecera por encima de la original
        ventana.title("Estadísticas de Ventas")
        ventana.geometry("1000x700")
        ventana.config(bg="#1e1e2e")

        #BARRA DE NAVEGACION
    # Barra superior
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
        estadisticas_boton_barra.bind("<Button-1>", lambda e: None)

        historial_boton_barra = tk.Label(menu_frame, text="📄 Historial", bg="#1e293b", width=18, height=2, font=("Arial", 12, "bold"), cursor="hand2", fg="#94a3b8")
        historial_boton_barra.grid(row=0, column=3, padx=10, pady=8)

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
