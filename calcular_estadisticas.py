import json
from datetime import datetime


def calcular_estadisticas():
    # Abrimos y leemos el archivo donde se guardan todas las ventas
    with open("registro.json", "r", encoding="utf-8") as bd:
        compras = json.load(bd)

    estaditicas = {}

    if len(compras["Ventas_registradas"]) == 0:
       estaditicas["Total_ventas"] = 0
       estaditicas["Total_ingresos"] = 0
       estaditicas["Cliente_lead"] = "Sin ventas"
       estaditicas["Mayor_producto"] = "Sin ventas"
       return estaditicas 
    
    

    # Total de ventas
    # Cuenta cuántas ventas hay registradas en total

    total_ventas = len(compras["Ventas_registradas"])
    estaditicas["Total_ventas"] = total_ventas

    # ---------- TOTAL DE INGRESOS ----------
    # Suma el campo "total" de cada venta (ya viene calculado al registrar)
    total_ingresos = sum(venta["total"] for venta in compras["Ventas_registradas"])
    estaditicas["Total_ingresos"] = total_ingresos

    # ---------- MEJOR CLIENTE ----------
    # contador_cliente guarda cuántas VENTAS hizo cada cliente
    contador_cliente = {}

    for pelota in compras["Ventas_registradas"]:
        cliente = pelota["cliente"]
        # si el cliente ya está en el diccionario, le sumamos 1 venta más
        if cliente in contador_cliente:
            contador_cliente[cliente] += 1
        else:
            contador_cliente[cliente] = 1

    mayor_cliente = max(contador_cliente, key=contador_cliente.get)
    estaditicas["Cliente_lead"] = mayor_cliente

    # ---------- PRODUCTO MÁS VENDIDO ----------
    # contador_producto guarda cuántas UNIDADES se vendieron de cada producto
    contador_producto = {}

    for product in compras["Ventas_registradas"]:
        # product es la venta completa (diccionario)
        producto = product["producto"]          # nombre del producto (texto)
        cantidad = float(product["cantidad"])    # ojo: usamos "product", no "producto"

        # si el producto ya existe, le sumamos la cantidad vendida en esta venta
        if producto in contador_producto:
            contador_producto[producto] += cantidad
        else:
            contador_producto[producto] = cantidad



        contador_dias = {}

        mayor_producto = max(contador_producto, key=contador_producto.get)
        
    estaditicas["Mayor_producto"] = mayor_producto

    # ---------- VENTAS POR DÍA ----------
    # Lista con los nombres de los días en orden
    nombres_dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

    # Contador que empieza en 0 para cada día
    contador_dias = {"Lun": 0, "Mar": 0, "Mié": 0, "Jue": 0, "Vie": 0, "Sáb": 0, "Dom": 0}

    for dia in compras["Ventas_registradas"]:
        # Agarramos la fecha de cada venta
        fecha = dia.get("fecha", None)
        if fecha:  # solo si la venta tiene fecha
            # Convertimos el texto a fecha real
            fecha_real = datetime.strptime(fecha, "%Y-%m-%d")
            # Sacamos el número del día (0=Lunes, 6=Domingo)
            dia_semana = fecha_real.weekday()
            # Convertimos el número al nombre
            nombre_dia = nombres_dias[dia_semana]
            # Sumamos 1 al día correspondiente
            contador_dias[nombre_dia] += 1

    estaditicas["Ventas_por_dia"] = contador_dias

    return estaditicas


    mayor_producto = max(contador_producto, key=contador_producto.get)
    estaditicas["Mayor_producto"] = mayor_producto

    return estaditicas