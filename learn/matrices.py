matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


# print(f" {matrix[0]} \n {matrix[1]} \n {matrix[2]}")
# print(f" {matrix[0][0]}, {matrix[1][0]}, {matrix[2][1]}, {matrix[0][2]}")

print("MOSTRAR TODOS LOS ELEMENTOS DE LA MATRIZ LISTA POR LISTA")
for row in matrix:
    print(row)
print("MOSTRAR TODOS LOS ELEMENTOS DE LA MATRIZ POR FILA")
for row in matrix:
    for element in row:
        print(element)
print("MOSTRAR TODOS LOS ELEMENTOS DE LA MATRIZ EN COLUMNAS")
for row in matrix:
    for element in row :
        print(element, end=" ")
    print()

