
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a=b
        b=a+b
    return fib_series

# Llamada a la función para obtener los primeros 10 números de la serie de Fibonacci
n = 10
resultado = fibonacci(n)
print(resultado)
