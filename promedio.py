def calcular_promedio(arreglo):
    if len(arreglo) == 0:
        return 0 
        
    suma= sum(arreglo)
    
    x= suma/len(arreglo)
    
    return x