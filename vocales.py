def verificar_vocales(cadena):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    
    # Contador para las vocales
    contador_vocales = 0
    
    # Contar las vocales en la cadena
    for letra in cadena:
        if letra in vocales:
            contador_vocales += 1
        # Si ya hay dos vocales, podemos salir del bucle
        if contador_vocales >= 2:
            break
    
    # Verificar si hay dos o más vocales
    if contador_vocales >= 2:
        print(cadena)
    else:
        print("No existe")




