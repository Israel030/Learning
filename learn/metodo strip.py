''' 
Metodo strip():  se utiliza para eliminar los espacios en blanco (espacios, tabulaciones, saltos de línea y caracteres) al inicio y al final de una cadena. 
Metodo rstrip(): se utiliza para eliminar caracteres (espacios en blanco u otros caracteres específicos) desde el lado derecho (final) de una cadena de texto.
Metodo istitle(): se utiliza para verificar si una cadena tiene un formato de título.
Metodo title(): se utiliza para convertit un texto en un titulo
Metodo isLower(): se utiliza para verificar si todos los caracteres en una cadena están en minúsculas. 
Metodo lower(): se utiliza para convertir un texto en minusculas 
Metodo isupper(): se utiliza para verificar todos los caracteres en una cadena estan en mayuscula
Metodo upper(): se utiliza oara convertir todos los carcateres en una cadena en mayusculas
Metodo swapcase(): una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa.
Metodo capitalize(): devuelve una cadena donde el primer carácter está en mayúsculas y el resto en minúsculas.
Metodo center(): se utiliza para centrar una cadena dentro de un ancho especificado.
Metodo Ijust(): oma un número que especifica la longitud deseada de la cadena como parámetro requerido y un carácter como parámetro opcional.
Metodo rjust(): agrega el carácter opcional a la izquierda de la cadena hasta que la cadena tenga la longitud deseada.
Metodo count(): se utiliza para contar cuántas veces aparece un elemento en una secuencia (como una cadena, una lista o una tupla).
Metodo startswith(): se utiliza para indicar si una cadena de texto comienza con los caracteres de una cadena de texto concreta, devolviendo true o false según corresponda
Metodo endswith(): se utiliza para saber si una cadena de texto termina con los caracteres de una cadena indicada.
Substrings 
'''

valor = ",,,,,sszzoo.....Strip....iii"
subcadena = "you are the moon"
strip = valor.strip(",.szoi")
rstrip = valor.rstrip(".i")
istitle = valor.istitle()
print("Este es el metodo",strip+
     "Este es el metodo rstrip",rstrip+
     "Este es el metodo rstrip",istitle)
print("esta es una subcadena: ",subcadena[3:9])
