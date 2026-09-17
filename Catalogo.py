# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:09:25 2026

@author: Iliev
"""

def catalogo() ->dict:
    """Carga el catalogo de los productos disponibles, y lo declaramos
       como diccionario   
    """
    return{
        "P001" : {"Nombre" : "Cafe", "Precio" : 45.0, "Stock" : 20}, 
        "P002" : {"Nombre" : "Te", "Precio" : 30.0, "Stock" : 15},
        "P003" : {"Nombre" : "Galletas",  "Precio" : 25.0, "Stock" : 15}
        #Se podrian agregar mas productos    
        }
