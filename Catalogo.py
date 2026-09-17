def catalogo() -> dict:
    """Carga el catalogo de los productos disponibles, y lo declaramos
       como diccionario   
    """
    return {
        "P001": {"nombre": "Cafe", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Te", "precio": 30.0, "stock": 15},
        "P003": {"nombre": "Galletas", "precio": 25.0, "stock": 15}
        #Se podrian agregar mas productos    
        }

def mostrar_catalogo(catalogo):
    """Imprime una tabla con los productos disponibles: id, nombre,
    precio y stock actual.
    """
    print(f"{'ID':<6}{'Producto':<15}{'Precio':<10}{'Stock':<6}")
    for id_producto, datos in catalogo.items():
        print(f"{id_producto:<6}{datos['nombre']:<15}{datos['precio']:<10.2f}{datos['stock']:<6}")