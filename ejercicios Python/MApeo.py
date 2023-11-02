''' 1.	Se tiene una función que entrega valores en 0 y 1. 
Escribe el código que convierta los valores obtenidos entre 32 y 100. 
Es decir, si la función me regresa un valor de 0.5, el código me debe regresar como salida el valor de 66. 
Si la función regresa el valor de 0, el código debe regresar el valor de 32. Etc,
'''

def funcion(valor):
    if valor < 0:
        valor = 0
    elif valor > 1:
        valor = 1
    return int(valor * (100-32)+32)
    
entrada = 0.5
salida = funcion(entrada)
print(salida)

entrada = 1
salida = funcion(entrada)
print(salida)