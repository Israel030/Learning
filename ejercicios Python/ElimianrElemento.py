lista = ["A","B","b","c","E","E","f"]

print(lista)

delCar = input("Introduce elemento a eliminar: ")

for i in lista:
    if delCar.lower() in lista:
        lista.remove(delCar.lower())
    elif delCar.upper() in lista:
        lista.remove(delCar.upper())
print(lista)
