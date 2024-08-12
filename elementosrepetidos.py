def verificar_repetidos(lista):
    # Convertir la lista en un conjunto para eliminar duplicados
    conjunto_sin_repetidos = set(lista)
    
    # Comparar la longitud de la lista original con la longitud del conjunto
    if len(lista) == len(conjunto_sin_repetidos):
        print("No existen elementos repetidos")
    else:
        print("Sí existen elementos repetidos")

# Ejemplos de uso

