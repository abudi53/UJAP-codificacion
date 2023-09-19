import base64

# Guia para encriptacion base64: 

# 1: Obtener el valor ASCII de cada caracter del texto a encriptar
# 2: Convertir el valor ASCII a binario
# 3: Concatenar todos los valores binarios
# 4: Dividir la cadena de binarios en grupos de 6 bits
# 5: Convertir cada grupo de 6 bits a decimal
# 6: Convertir cada decimal a base64

# Guia para encriptacion cesar:

# 1: Obtener el valor ASCII de cada caracter del texto a encriptar
# 2: Sumarle 12 al valor ASCII de cada caracter
# 3: Devolver el caracter correspondiente al valor ASCII.


def encriptador(texto):
    # Encriptación con cifrado César
    cesar = ""
    for letra in texto:
        cesar += chr((ord(letra) + 12) % 256) # Devuelve el caracter unicode correspondiente al número
    # Encriptación en base64
    base64_str = base64.b64encode(cesar.encode('utf-8'))
    print(base64_str)
    
    # Conversión a bits
    bits = ''.join(format(byte, '08b') for byte in base64_str)
    
    return bits


