def dibujo(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2*i + 1))

    tronco = n//2
    for i in range(tronco):
        print(" " * (n - 1) + "*")


n = int(input('Ingresa las filas del pino: '))
dibujo(n)