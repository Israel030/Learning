sufijos = {1000: ["KB", "MB", "GB"], 1024: ["KiB", "MiB", "GiB"]}

def tamanioAprox(tamanio, unkilibytees1024=True):

    if tamanio < 0:
        raise ValueError("El número debe ser no negativo.")

    multiplo = 1024 if unkilibytees1024 else 1000
    for sufijo in sufijos[multiplo]:
        tamanio /= multiplo

        if tamanio < multiplo:
            return '{:.1f} {}'.format(tamanio, sufijo)

    raise ValueError("Número demasiado grande")

if __name__ == '__main__':
    print(tamanioAprox(100000000000, False))
    print(tamanioAprox(100000000000))
