# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:12:55 2026

@author: Iliev
"""

def calcular_subtotal(carrito, catalogo):
    """Recorre el carrito y suma precio*cantidad de cada producto
    usando los precios del catalogo.
    """
    subtotal = 0.0
    for id_producto, cantidad in carrito:
        precio = catalogo[id_producto]["precio"]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento(subtotal, tipo_descuento):
    """Aplica una regla de descuento sobre el subtotal segun el tipo
    solicitado. Regresa el total final.
    """
    reglas = {
        "3x2": 0.0,      # se resuelve aparte, requiere cantidades por producto
        "porcentaje": 0.10,
        "ninguno": 0.0
    }
    
    if tipo_descuento not in reglas:
        print("Tipo de descuento no reconocido, no se aplica descuento")
        return subtotal
    
    if tipo_descuento == "porcentaje":
        descuento = subtotal * reglas["porcentaje"]
        total = subtotal - descuento
        print(f"Se aplico {reglas['porcentaje']*100:.0f}% de descuento")
        return total
    elif tipo_descuento == "ninguno":
        return subtotal
    else:
        print("Regla de descuento aun no implementada")
        return subtotal