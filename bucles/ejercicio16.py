contrasena_correcta = "python123"
ok = False
for ok = False:
    contrasena_usuario = input("Introduce la contraseña: ")
    
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
else:
    print("Has alcanzado el número máximo de intentos.")
