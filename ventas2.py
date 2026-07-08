
import tkinter as tk
from tkinter import ttk



class TarjetaVenta(tk.Frame):
    """Una 'card' individual con los datos de una venta."""

    def __init__(self, master, venta, on_editar, on_eliminar):
        super().__init__(
            master,
            bg="#242436",
            highlightbackground="#3a3a55",
            highlightthickness=1,
            padx=12, pady=10
        )
        self.venta = venta

        titulo = tk.Label(
            self, text=f"Venta #{venta['id']}",
            bg="#242436", fg="#ffffff",
            font=("Segoe UI", 11, "bold"), anchor="w"
        )
        titulo.pack(fill="x")

        campos = [
            ("Cliente", venta["cliente"]),
            ("Producto", venta["producto"]),
            ("Cantidad", venta["cantidad"]),
            ("Precio", f"${venta['precio']}"),
            ("Total", f"${venta['total']}"),
            ("Fecha", venta["fecha"]),
        ]
        for etiqueta, valor in campos:
            fila = tk.Frame(self, bg="#242436")
            fila.pack(fill="x", pady=1)
            tk.Label(fila, text=f"{etiqueta}:", bg="#242436",
                     fg="#9a9ac0", font=("Segoe UI", 9),
                     anchor="w", width=9).pack(side="left")
            tk.Label(fila, text=valor, bg="#242436",
                     fg="#e6e6f0", font=("Segoe UI", 9),
                     anchor="w").pack(side="left", fill="x", expand=True)

        botones = tk.Frame(self, bg="#242436")
        botones.pack(fill="x", pady=(8, 0))

        tk.Button(
            botones, text="Editar", bg="#6c63ff", fg="white",
            relief="flat", activebackground="#5a52d5",
            command=lambda: on_editar(self.venta)
        ).pack(side="left", expand=True, fill="x", padx=(0, 4))

        tk.Button(
            botones, text="Eliminar", bg="#ff5a3c", fg="white",
            relief="flat", activebackground="#d9452b",
            command=lambda: on_eliminar(self.venta)
        ).pack(side="left", expand=True, fill="x", padx=(4, 0))


class HistorialVentas(tk.Frame):
    """Contenedor con scroll que organiza las tarjetas en columnas."""

    def __init__(self, master):
        super().__init__(master, bg="#141420")
        self.pack(fill="both", expand=True)

        # --- Canvas + Scrollbar ---
        self.canvas = tk.Canvas(self, bg="#141420", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Frame interno donde van las tarjetas
        self.contenedor = tk.Frame(self.canvas, bg="#141420")
        self.ventana_id = self.canvas.create_window(
            (0, 0), window=self.contenedor, anchor="nw"
        )

        self.contenedor.bind("<Configure>", self._actualizar_scrollregion)
        self.canvas.bind("<Configure>", self._reorganizar_al_redimensionar)

        # Scroll con la rueda del mouse
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.columnas_actuales = 1
        self.renderizar(ventas)

    def _actualizar_scrollregion(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _reorganizar_al_redimensionar(self, event):
        # Ajusta el ancho de la ventana interna al ancho del canvas
        self.canvas.itemconfig(self.ventana_id, width=event.width)

        # Calcula cuántas columnas caben según el ancho disponible
        columnas = max(1, event.width // ANCHO_TARJETA)
        if columnas != self.columnas_actuales:
            self.columnas_actuales = columnas
            self.renderizar(ventas)

    def renderizar(self, lista_ventas):
        # Limpia tarjetas anteriores
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        columnas = self.columnas_actuales
        for i in range(columnas):
            self.contenedor.grid_columnconfigure(i, weight=1, uniform="col")

        for index, venta in enumerate(lista_ventas):
            fila, col = divmod(index, columnas)
            tarjeta = TarjetaVenta(
                self.contenedor, venta,
                on_editar=self.editar_venta,
                on_eliminar=self.eliminar_venta
            )
            tarjeta.grid(row=fila, column=col, padx=8, pady=8, sticky="nsew")

        self._actualizar_scrollregion()

    def editar_venta(self, venta):
        print("Editar:", venta)

    def eliminar_venta(self, venta):
        ventas.remove(venta)
        self.renderizar(ventas)


if __name__ == "__main__":
    screen = tk.Tk()
    screen.title("Historial de Ventas")
    screen.geometry("900x600")
    screen.configure(bg="#141420")
    HistorialVentas(screen)
    screen.mainloop()
