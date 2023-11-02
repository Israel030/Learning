lista = []

longitud = int(input("Ingresa longitud de la lista: "))


for i in range(longitud):
    lista.append(int(input("Introduce un numero: ")))

print(f"Estos son los elementos de la lista: {lista} \nLA suma es: {sum(lista)}")