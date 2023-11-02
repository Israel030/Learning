''' Desarrollar un programa que solicite un número
entero desde teclado al usuario, posteriormente, el
programa deberá determinar e indicar a través de un
mensaje, si el número introducido es par o impar.
'''
numero = int(input("Ingresa un número: "))

if numero%2==0:
    print("El numero ",numero, "es par")
elif numero%2==1:
    print("El numero ",numero,"es impar")
    
