# Accediendo a un diccionario
diccionario = {"a": 1,

               "b": 2,

               "c": 3,

               "d": {'pr': 45}}
print(diccionario)
print(f"Clave a: {diccionario['a']}")


# METODO ITEMS() = ver las claves y valores de nuestros diccionarios
print("\nMETODO ITEMS")
print(diccionario.items())
list_items = list(diccionario.items())
print("Diccionario convertido a lista: ", list_items)
print(f"Posicion 1 de la lista items: {list_items[0]}")


# METODO KEYS() = obtener una lista de todas las claves de un diccionario
print("\nMETODO KEYS")
print(f"Llaves de diccionario:  {diccionario.keys()}")
valores = list(diccionario.keys())
print(f"Claves convertidas a lista: {valores}")
print(f"Posicion 1 de la lista keys: {valores[0]}")


# METOD VALUES() = obtener una lista de todos los valores del diccionario
print("\nMETODO VALUES")
print(f"Valores de diccionario:  {diccionario.values()}")
valores = list(diccionario.values())
print(f"valores convertidas a lista: {valores}")
print(f"Posicion 1 de la lista valores: {valores[0]}")

#METODO CLEAR() = eliminar todos los elementos de un objeto 
employes = {'Isra': {'edad': 23, 'salario': 1200},
            'Xime': {'edad': 24, 'salario': 1200}
            }
print("\nMETODO CLEAR")
print(f"Diccionario original de empleados: {employes}")
# employes.clear()
print(f"Diccionario de empleados actualizado: {employes}")

#METODO COPY() = copia un objeto sin afectar al original 
print("\nMETODO COPY")
print(f"Diccionario original de empleados: {employes}")
copia_employes = employes.copy()
print(f"Copia de diccionario employes: {copia_employes}")
copia_employes.clear()
print(f"Copia limpiada de employes: {copia_employes}")

#METODO FROMEKEYS() Crea un nuevo diccionario con claves de una secuencia dada
print("\nMETODO FROMKEYS")
sequence = ['uno', 'dos','tres']
value = 5
name_dic = dict.fromkeys(sequence, value)
print(name_dic)