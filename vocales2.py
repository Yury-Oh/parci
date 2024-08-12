def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

def encontrar_palabras_con_vocales(cadena):
    palabras = cadena.split()
    palabras_con_vocales = [palabra for palabra in palabras if contar_vocales(palabra) >= 2]
    return palabras_con_vocales

# Ejemplo de uso
cadena = "Este es un ejemplo de cadena con varias palabras"
resultado = encontrar_palabras_con_vocales(cadena)

print("Palabras con dos o más vocales:", resultado)
