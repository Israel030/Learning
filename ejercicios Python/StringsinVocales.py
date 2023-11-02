'''
Desarrollar un programa que solicita una frase desde teclado, así
como un caracter en especifico, ya sea una letra, un numero o 
caracter especial.
Posteriormente, el programa debera imprimir en pantalla la frase
desde teclado, "sin vocales", y en caso de que el caracter especifico
sea parte de la frase, el bucle debera finalizar su ejecucion.

Vid. 12,21,24,31
'''

frase = input("ingresa una frase: ")
letter = input("letra: ")

for letra in frase:
    if letra.lower()==letter.lower():
        break
    elif letra.lower()=="a":
        continue
    elif letra.lower()=="e":
        continue
    elif letra.lower()=="i":
        continue
    elif letra.lower()=="o":
        continue
    elif letra.lower()=="u":
        continue
    print(letra,end=(""))