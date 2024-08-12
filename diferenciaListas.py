def elementos_unicos(lista1, lista2):
    # Convertir la segunda lista en un conjunto para optimizar la búsqueda
    conjunto_lista2 = set(lista2)
    
    # Crear una lista con los elementos que están en lista1 y no en lista2
    unicos = [elemento for elemento in lista1 if elemento not in conjunto_lista2]
    
    return unicos




