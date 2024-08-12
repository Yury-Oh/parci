def calcular_mediana(arreglo):
    # Ordenar el arreglo
    arreglo_ordenado = sorted(arreglo)
    
    # Obtener el tamaño del arreglo
    n = len(arreglo_ordenado)
    
    # Determinar la mediana
    if n % 2 == 1:  # Si el número de elementos es impar
        mediana = arreglo_ordenado[n // 2]
    else:  # Si el número de elementos es par
        mediana = (arreglo_ordenado[(n // 2) - 1] + arreglo_ordenado[n // 2]) / 2
    
    return mediana