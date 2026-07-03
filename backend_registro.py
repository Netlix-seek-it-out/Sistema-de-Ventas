import json
from datetime import datetime  # para trabajar con fechas


def calcular_estadisticas():
    # Abrimos y leemos el archivo donde se guardan todas las ventas
    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)

    estaditicas = {}

    # Si no hay ventas, devolvemos valores por defecto
    if len(compras["Ventas_registradas"]) == 0:
        estaditicas["Total_ventas"] = 0
        estaditicas["Total_ingresos"] = 0
        estaditicas["Cliente_lead"] = "Sin ventas"
        estaditicas["Mayor_producto"] = "Sin ventas"
        estaditicas["Ventas_por_dia"] = {"Lun": 0, "Mar": 0, "Mié": 0, "Jue": 0, "Vie": 0, "Sáb": 0, "Dom": 0}
        return estaditicas

    # ---------- TOTAL DE VENTAS ----------
    # Cuenta cuántas ventas hay registradas en total
    total_ventas = len(compras["Ventas_registradas"])
    estaditicas["Total_ventas"] = total_ventas

    # ---------- TOTAL DE INGRESOS ----------
    # Suma el campo "total" de cada venta
    total_ingresos = sum(venta["total"] for venta in compras["Ventas_registradas"])
    estaditicas["Total_ingresos"] = total_ingresos

    # ---------- MEJOR CLIENTE ----------
    # Cuenta cuántas ventas hizo cada cliente
    contador_cliente = {}
    for pelota in compras["Ventas_registradas"]:
        cliente = pelota["cliente"]
        if cliente in contador_cliente:
            contador_cliente[cliente] += 1
        else:
            contador_cliente[cliente] = 1

    # max() busca el cliente con más ventas
    mayor_cliente = max(contador_cliente, key=contador_cliente.get)
    estaditicas["Cliente_lead"] = mayor_cliente

    # ---------- PRODUCTO MÁS VENDIDO ----------
    # Suma cuántas unidades se vendieron de cada producto
    contador_producto = {}
    for product in compras["Ventas_registradas"]:
        producto = product["producto"]
        cantidad = float(product["cantidad"])
        if producto in contador_producto:
            contador_producto[producto] += cantidad
        else:
            contador_producto[producto] = cantidad

    mayor_producto = max(contador_producto, key=contador_producto.get)
    estaditicas["Mayor_producto"] = mayor_producto

    # ---------- VENTAS POR DÍA ----------
    # Lista con los nombres de los días en orden (0=Lun, 1=Mar... 6=Dom)
    nombres_dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

    # Empezamos el contador en 0 para cada día
    contador_dias = {"Lun": 0, "Mar": 0, "Mié": 0, "Jue": 0, "Vie": 0, "Sáb": 0, "Dom": 0}

    for dia in compras["Ventas_registradas"]:
        # Agarramos el texto de la fecha de cada venta
        fecha = dia.get("fecha", None)

        if fecha:  # si la venta tiene fecha guardada
            # Convertimos el texto "2026-07-02" a objeto de fecha real
            fecha_real = datetime.strptime(fecha, "%Y-%m-%d") #  %Y es el año, %m es el mes, %d es el día.
            # Sacamos el número del día (0=Lunes, 6=Domingo)
            dia_semana = fecha_real.weekday()
            # Convertimos el número al nombre del día
            nombre_dia = nombres_dias[dia_semana]
            # Sumamos 1 al contador de ese día
            contador_dias[nombre_dia] += 1

    estaditicas["Ventas_por_dia"] = contador_dias

    return estaditicas