def agregar_producto(carrito, catalogo, id_producto, cantidad):
    """Valida stock, descuenta inventario y agrega el producto a la lista 
    del carrito.
    """
    if id_producto not in catalogo:
        print("El producto a comprar no existe")
        return False
    if cantidad == 0:
        print("Se debe comprar cuando menos 1 articulo")
        return False
    
    """Aqui necesitamos leer la cantidad de stock, para ello debemos leer el 
    diccionario
    """
    x = catalogo[id_producto]
    if x["stock"] < cantidad:
        print(f"El numero de {id_producto} disponible es {cantidad}")
        return False
    
    #Le restamos la cantidad de producto comprada al stock disponible
    x["stock"] = x["stock"] - cantidad
    
    #Avisamos qie el producto se anadio al carro
    print(f"Producto {x['nombre']} agregado al carrito.")
    return True