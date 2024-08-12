from elementosrepetidos import verificar_repetidos
from vocales import verificar_vocales
from diferenciaListas import elementos_unicos
from promedio import calcular_promedio
from mediana import calcular_mediana
from vocales2 import *

def main():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    v = [-8, 2, 3]
    w = [4, 5, 6]
    y = ("Hola")
    yury = ("no")
    cadena = "Este es un ejemplo de cadena con varias palabras, Jungkook es el amor de mi vida jajaja"

    # calcular_promedio
    promedio = calcular_promedio(v)
    print(f"Promedio: {promedio}")
    
    # calcular mediana
    resultado_mediana = calcular_mediana(w)
    print(f"La mediana es: {resultado_mediana}")

    #vocales repetidas
    verificar_vocales(y)


    verificar_vocales(yury)

    #elementos de una lista que no estan en otra

    resultado = elementos_unicos(lista1, lista2)
    print("Elementos que están en la primera lista y no en la segunda:", resultado)

    #elementos repetidos

    verificar_repetidos([1, 2, 3, 4, 5])

    # Ejemplo de uso vocales2

    resultado = encontrar_palabras_con_vocales(cadena)
    print("Palabras con dos o más vocales:", resultado)



if __name__ == "__main__":
    main()