import decriptador, encriptador

#Menu principal

while True:
    print("Bienvenido al programa de encriptación")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")
    opcion = input("Introduce una opción: ")
    if opcion == "1":
        texto = input("Introduce el texto a encriptar: ")
        texto_encriptado = encriptador.encriptador(texto)
        print("Texto encriptado: ", texto_encriptado)
    elif opcion == "2":
        texto_encriptado = input("Introduce el texto a desencriptar: ")
        texto_original = decriptador.decriptador(texto_encriptado)
        print("Texto original: ", texto_original)
    elif opcion == "3":
        break
    else:
        print("Opción incorrecta")
    print("")