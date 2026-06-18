import tkinter as tk 

ventana = tk.Tk()
ventana.title("resumen de ventana ")
ventana.geometry("900x650")
ventana.config(bg="#1e1e2e")

titulo = tk.Label(ventana,text="📊 Estadisticas",font=("Arial",22,"bold"),bg="#1e1e2e",fg="#cdd6f4")
titulo.pack(pady=20 )

tarjetas_1 = tk.Frame(ventana,bg="#36A126",width=200,height=120)

tarjetas_1.place(x=150, y=100)

tarjetas_1.pack_propagate(False)



tex_targeta1= tk.Label(tarjetas_1,text= "🛒 Total ventas",font=("Arial",14,"bold"),bg="#36A126",fg="#FFFDFD")

tex_targeta1.pack(pady=(30,5))



tarjetas_2= tk.Frame(ventana,bg="#8E44AD",width=200,height=120)

tarjetas_2.place(x=450, y=100)

tarjetas_2.pack_propagate(False)



tex_targeta2= tk.Label(tarjetas_2,text= "🏆 Producto Top",font=("Arial",14,"bold"),bg="#8E44AD",fg="#FFFDFD")

tex_targeta2.pack(pady=(30,5))



tarjetas_3= tk.Frame(ventana,bg="#E67E22",width=200,height=120)

tarjetas_3.place(x=150, y=260)

tarjetas_3.pack_propagate(False)



tex_targeta3= tk.Label(tarjetas_3,text= "👤 Cliente VIP",font=("Arial",14,"bold"),bg="#E67E22",fg="#FFFDFD")

tex_targeta3.pack(pady=(30,5))



tarjetas_4= tk.Frame(ventana,bg="#1E88E5",width=200,height=120)

tarjetas_4.place(x=450, y=260)

tarjetas_4.pack_propagate(False)



tex_targeta4= tk.Label(tarjetas_4,text="💰 Ingresos" ,font=("Arial",14,"bold"),bg="#1E88E5",fg="#FFFDFD")

tex_targeta4.pack(pady=(30,5))











ventana.mainloop()