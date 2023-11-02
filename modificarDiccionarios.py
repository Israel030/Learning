#modificarDiccionarios
employes = {'Isra': {'edad': 23, 'salario': 1200},
            'Xime': {'edad': 24, 'salario': 1200}
            }
print(f"Diccionario original: {employes}")

employes['Beto'] = {'edad': 21, 'salario': 3054}
print(f"Diccionario modificado: {employes}")
employes['Beto'] = {'edad': 25, 'salario': 0000}
print(f"Salario de Beto modificado: {employes}")