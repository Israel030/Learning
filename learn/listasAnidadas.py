'''
Las listas anidadas osn listas dentro de otras listas.
'''
lista = [1,"a",True,[1,2,3,['a','f','g','e']]]
print(lista)
print("Accediendo a elemento de la primer lista ",lista[3])
print("Accediento al elemento de la segunda lista",lista[3][1])
print("Accediento al elemento de la tercera lista",lista[3][3][1])

