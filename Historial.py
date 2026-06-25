import tkinter as tk

screen = tk.Tk()
screen.title("Historial")
screen.geometry("1300x900")
screen.configure(bg="#1e1e2e")

# barra del naveagdors
nav = tk.Frame(screen, bg="#252535", height=40)
nav.pack(fill="x")
tk.Label(nav, text="¡Indago!", bg="#252535", fg="#7b6cf6", font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=8)

# Titulo
tk.Label(screen, text="Historial", bg="#1e1e2e", fg="white", font=("Arial", 16, "bold")).pack(anchor="w", padx=20, pady=(15, 5))

# Tarjeta
card = tk.Frame(screen, bg="#2a2a3e")
card.pack(fill="both", expand=True, padx=20, pady=5)

for item in ["Registro", "Estadísticas", "Historial"]:
    tk.Label(nav, text=item, bg="#252535", fg="#a0a0c0", font=("Arial", 9)).pack(side="left", padx=10)


mensaje = tk.Label(
    card,
    text="Tus registros",
    bg="#2a2a3e",
    fg="white",
    font=("Arial", 11, "bold")
)
mensaje.place(relx=0.5, rely=0.5,
              anchor="center")

dias= ["lunes:","martes:","miercoles:","jueves:","viernes:","sabado:","domingo:"]

for dia in dias:
    tk.Label(card, text=dia, bg="#2a2a3e", fg="white", font=("Arial", 12,)).pack(anchor="w", padx=20, pady=2)

# Resumen
tk.Label(card, text="Resumen", bg="#2a2a3e", fg="white", font=("Arial", 11, "bold")).pack(anchor="w", padx=15, pady=(10, 2))
screen.mainloop()