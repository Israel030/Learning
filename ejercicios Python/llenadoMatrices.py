rows = int(input("cuantas filas tendra la matriz?: "))
columns = int(input("cuantas columnas tendra la matriz?: "))
matrix = []

for rowPosition in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila {rowPosition}: ")))
    matrix.append(row)


