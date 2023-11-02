number_matrix = int(input("Cuantas matrices quieres sumar: "))

if number_matrix > 1:
    filas = int(input("Cuantas filas tendran las matrices: "))
    columnas = int(input("Cuantas columnas tendran las matrices: "))
    matrix_list = []

    # Llenado de matrices
    for number in range(number_matrix):
        matriz = []
        for row in range(filas):
            new_row = []
            for col in range(columnas):  # Cambio de 'columnas' a 'col'
                new_row.append(
                    int(input(f"Introduce un elemento para la matriz {number + 1} fila {row}, columna {col}: ")))

            matriz.append(new_row)
        matrix_list.append(matriz)
    
    #suma de Matrices
    matrix = []
    for row in range(filas):
        new_row = []
        for col in range(columnas):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list)):
                sum_matrix += matrix_list[matrix_position][row][col]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)

    #imprimir matrices
    for matrix_row in range(filas):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_row != 1:
                print(f"{matrix_list[matrix_list_position]}{matrix_row}",end="  ")
            else:
                if matrix_list_position < len(matrix_list) -2:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}",end=" + ")
                elif matrix_list_position < len(matrix_list) -1:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}",end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}",end=" ")                 
        print()

else:
    print("Se necesitan más de una matriz para la suma.")
