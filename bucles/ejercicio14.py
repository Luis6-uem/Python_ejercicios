suma = 0

while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero

print(f"Suma total: {suma}")
