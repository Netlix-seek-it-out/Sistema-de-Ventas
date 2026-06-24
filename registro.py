import tkinter as tk

root = tk.Tk()
root.title("Sistemas de ventas")
root.state("zoomed")  # Pantalla completa en Windows
root.configure(bg="#1e1e2e")
root.resizable(True, True)

# Titulo
tk.Label(root, text="Registrar venta",
         bg="#1e1e2e", fg="#cdd6f4",
         font=("Segoe UI", 20, "bold")).pack(pady=(40, 30))

# Campo con las 6 etiquetas
form_frame = tk.Frame(root, bg="#1e1e2e")
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
    entry.pack(fill="x", pady=(4, 22), ipady=10)
    entries[key] = entry

# Columna izquierda
make_field(left_col,  "num_venta", "Numero de venta:")
make_field(left_col,  "cliente",   "Nombre del cliente:")
make_field(left_col,  "producto",  "Producto vendido:")

# Columna derecha
make_field(right_col, "cantidad",  "Cantidad:")
make_field(right_col, "precio",    "Precio unitario:")
make_field(right_col, "total",     "Total:")

# Boton
def guardar():
    lbl_status.config(text="Venta guardada correctamente.")

btn = tk.Button(root, text="Guardar Venta",
                bg="#7c6af7", fg="#ffffff",
                activebackground="#9a8cff", activeforeground="#ffffff",
                relief="flat", font=("Segoe UI", 13, "bold"),
                cursor="hand2", command=guardar)
btn.pack(ipadx=40, ipady=12, pady=(20, 0))

lbl_status = tk.Label(root, text="", bg="#1e1e2e",
                       fg="#a6e3a1", font=("Segoe UI", 11))
lbl_status.pack(pady=12)

root.mainloop()
