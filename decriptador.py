import base64


def decriptador(texto_encriptado):
    # Conversión de bits a base64
    base64_str = bytes(int(texto_encriptado[i:i+8], 2) for i in range(0, len(texto_encriptado), 8))
    
    # Decodificación en base64
    cesar = base64.b64decode(base64_str).decode('utf-8')
    
    # Decodificación con cifrado César
    texto_original = ""
    for letra in cesar:
        texto_original += chr((ord(letra) - 12) % 256)
    
    return texto_original