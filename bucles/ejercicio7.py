cadena = "Python es Genial"
contador = 0  # Asegúrate de inicializar el contador aquí
vocales = "aeiouAEIOU"  # Cambia la lista a una cadena simple con las vocales

for caracter in cadena:
    if caracter in vocales:  # Verifica si el carácter está dentro de las vocales
        contador += 1

print(f"La palabra tiene {contador} vocales")
