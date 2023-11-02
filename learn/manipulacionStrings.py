
#ASIGNACION

mensaje = "Hola"
mensaje+=" "
mensaje+="Israel "
print(mensaje)

#CONCATENACION  
mensaje = "Hola"
mensaje2 = "lindo"
print(mensaje+" "+mensaje2)

num1 = 3
num2 = 3
res = num1+num2
print("la suma es: "+str(res))

#BUSQUEDA
#la funcion find hace el recorrido en la cadena mensaje
print("BUSQUEDA:")
mensaje = "La famosa banda de rock se separó, al menos por un tiempo. Los integrantes declararon en diversos medios que no hubo una pelea, sino que quieren trabajar un tiempo como solitas. Además, en una rueda de prensa, el representante dijo que es probable que el año próximo los músicos se vuelvan a juntar para hacer una gira."
prueba = "hubo una pelea"
buscar=mensaje.find("rock")
print(buscar)

#EXTRACCION
extraer = mensaje[3:16]
print(extraer)

#COMPARACION
print(mensaje != mensaje2)