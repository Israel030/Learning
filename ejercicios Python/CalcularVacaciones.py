'''La compañía multinacional Rappi, solicita un
sistema que determine los dias de vacaciones a
los que tiene derecho un trabajador, tomando en
cuenta las siguientes características.
Existen tres departamentos dentro de la compañia con
sus respectivas claves.
1. Departamento de Atención al cliente. (Clave 1)
2. Departamento de Logística. (Clave 2)
3. Gerencia. (Clave 3)
'''

clave = int(input("Ingresa tu clave: "))
antiguedad = float(input("Años trabajando: "))

if clave ==1:
    if antiguedad ==1 and antiguedad <= 2:
        print("6 dias de vacaciones")
    elif antiguedad ==2 and antiguedad <= 6:
        print("14 dias de vacaciones")
    elif antiguedad >= 6:
        print("20 dias de vacaciones")
    else:
        print("No mereces vacaciones!")
elif clave==2:
    if antiguedad ==1 and antiguedad <= 2:
        print("7 dias de vacaciones")
    elif antiguedad ==2 and antiguedad <= 6:
        print("15 dias de vacaciones")
    elif antiguedad >= 6:
        print("22 dias de vacaciones")
    else:
        print("No mereces vacaciones!")
elif clave==3:
    if antiguedad ==1 and antiguedad <= 2:
        print("10 dias de vacaciones")
    elif antiguedad ==2 and antiguedad <= 6:
        print("20 dias de vacaciones")
    elif antiguedad >= 6:
        print("30 dias de vacaciones")
    else:
        print("No mereces vacaciones!")
else:
    print("Clave desconocida.")     