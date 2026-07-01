import json


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
    
    #else:

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

    # max() busca la clave (cliente) con el valor más alto en el diccionario
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

    mayor_producto = max(contador_producto, key=contador_producto.get)
    estaditicas["Mayor_producto"] = mayor_producto

    return estaditicas