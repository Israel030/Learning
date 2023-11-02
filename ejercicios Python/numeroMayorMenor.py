num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un número: "))
num3 = int(input("Ingresa un número: "))

if num1 > num2 and num1>num3:
    print("El numero ",num1," es el mayor")
elif num2 > num1 and num2 >num3:
    print("El numero ",num2," es el mayor")
elif num3 > num1 and num3 >num2:
    print("El numero ",num3," es el mayor")