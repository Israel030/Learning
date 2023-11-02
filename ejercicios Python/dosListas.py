lista = [1,2,3,4,5]
print(f"Lista de numeros: {lista}")


numerosEliminados = []
numerosEliminados.append(lista.pop(0))
numerosEliminados.append(lista.pop(-1))
print(f"Numeros actualizado: {lista}")
print(f"Numeros eliminados {numerosEliminados}")
