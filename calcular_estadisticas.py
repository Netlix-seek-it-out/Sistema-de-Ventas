import json


def calcular_estadisticas():    
    with open("registro.json", "r", encoding="utf-8") as bd:       
        compras = json.load(bd)

    estaditicas =  {}

    #Calculando el total
    total_ventas = len(compras["Ventas_registradas"])
    estaditicas["Total_ventas"] = total_ventas
    #return total_ventas

    # Sacando el cliente, y el producto más vendido
    contador_cliente = {} #este contador irá aumentando dependiendo de cuantas veces encunetre un valor repetido en un buclee

    for pelota in compras["Ventas_registradas"]:
        cliente = pelota["cliente"]
    #si el cliente existe, suma uno
        if cliente in contador_cliente:
            contador_cliente["cliente"] += 1
        else:
            contador_cliente["cliente"] = 1

    mayor_cliente = max(contador_cliente, key=contador_cliente.get)

    estaditicas["Cliente_lead"] = mayor_cliente


    #Mayor producto:

    contador_producto = {} #este contador irá aumentando dependiendo de cuantas veces encunetre un valor repetido en un buclee

    for product in compras["Ventas_registradas"]:
        producto = product["producto"]
    #si el pproduucto existe, suma uno
        if producto in contador_producto:
            contador_producto["producto"] += 1
        else:
            contador_producto["producto"] = 1
    #contador.get atrapa


    mayor_producto = max(contador_producto, key=contador_producto.get)
    estaditicas["Mayor_producto"] = mayor_producto

    return estaditicas

