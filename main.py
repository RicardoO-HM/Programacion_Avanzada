# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:43:50 2026

@author: Lap1
"""

from Catalogo import catalogo, mostrar_catalogo
from Carrito import agregar_producto, eliminar_producto
from Descuentos import calcular_subtotal, aplicar_descuento
from Ticket import generar_ticket


def main():
    productos = catalogo()
    carrito_compras = []
    
    while True:
        print("\n1. Ver catalogo")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Ver total y generar ticket")
        print("5. Salir")
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            mostrar_catalogo(productos)
        elif opcion == "2":
            id_producto = input("ID del producto: ")
            cantidad = int(input("Cantidad: "))
            agregar_producto(carrito_compras, productos, id_producto, cantidad)
        elif opcion == "3":
            id_producto = input("ID del producto a eliminar: ")
            eliminar_producto(carrito_compras, productos, id_producto)
        elif opcion == "4":
            if not carrito_compras:
                print("El carrito esta vacio")
                continue
            subtotal = calcular_subtotal(carrito_compras, productos)
            tipo_descuento = input("Tipo de descuento (porcentaje/ninguno): ")
            total = aplicar_descuento(subtotal, tipo_descuento)
            generar_ticket(carrito_compras, productos, total)
        elif opcion == "5":
            print("Gracias por su compra")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()