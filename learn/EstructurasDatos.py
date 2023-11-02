# LISTAS

listaVacia = ["r","p"]
vocales = ["a","e","i","u"]
numeros = [0,1,2,3,4,5]
decimales = [1.1,1.2,1.3,1.4,1.5]
booleanos = [True,False,False,True]
listaHeterogenea = [1,"Hola",True,3.1416]

#METODOS
vocales.insert(3,"o")
del vocales[0:3]
decimales.reverse()
booleanos.pop(2)
booleanos.remove(True)
listaHeterogenea[2] = False
listaVacia.append("Espacio")
numeros.sort(reverse=True)


print("Lista vavia: ",listaVacia)
print("\n Lista homogenea: ",vocales)
print("\n Numeros: ",numeros)
print("\n Decimales: ",decimales)
print("\n Booleanos: ",booleanos)
print("\n Lista Heterogenea: ",listaHeterogenea)
print(f"La letra u esta en la posicion: {vocales.index('u')}")
print(f"El metodo extend: {vocales.extend(listaVacia)}")