import re

largo = re.compile(r'.{8,}')
digito = re.compile(r'\d+')
letra_may = re.compile(r'[A-Z]+')
letra_min = re.compile(r'[a-z]+')
caracteres =  re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]')

validaciones = [(largo, "largo menor que ocho"),
                (digito, "no tiene digitos"),
                (letra_min, "no tiene letras minúsculas"),
                (letra_may, "no tiene letras mayúsculas"),
                (caracteres, "no tiene caracteres especiales")]

tests = [
   "ISraelnm10!",
   "israelnm10",
   "Calamardo",
   "111d2kmlk2b",
   "12fd"
]

for test in tests:
    valida = True
    for validacion, mensaje in validaciones:
        if not validacion.search(test):
            print(f"{test}: {mensaje}")
            valida = False

    if valida:
        print(f"{test} ok")