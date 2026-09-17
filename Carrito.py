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
        print(f"El numero de {id_producto} disponible es {x['stock']}")
        return False
    
    #Le restamos la cantidad de producto comprada al stock disponible
    x["stock"] = x["stock"] - cantidad
    
    #Buscamos si el producto ya esta en el carrito para acumular cantidad
    for i, (pid, cant_actual) in enumerate(carrito):
        if pid == id_producto:
            carrito[i] = (pid, cant_actual + cantidad)
            break
    else:
        carrito.append((id_producto, cantidad))
    
    #Avisamos que el producto se anadio al carro
    print(f"Producto {x['nombre']} agregado al carrito.")
    return True


def eliminar_producto(carrito, catalogo, id_producto):
    """Quita un producto del carrito y regresa el stock descontado
    al catalogo.
    """
    for i, (pid, cantidad) in enumerate(carrito):
        if pid == id_producto:
            catalogo[id_producto]["stock"] += cantidad
            del carrito[i]
            print(f"Producto {id_producto} eliminado del carrito.")
            return True
    
    print("El producto no esta en el carrito")
    return False