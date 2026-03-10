# Función para cifrar una sola letra
def cifrar_letra(letra, desplazamiento):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Buscamos la posición de la letra en el abecedario (siempre en mayúsculas)
    posicion = abc.find(letra.upper())
    
    # Si la letra no está en el abecedario (ej. un número o símbolo), se devuelve igual
    if posicion == -1: 
        return letra
        
    # Calculamos la nueva posición usando el operador módulo (%)
    # Esto hace que si llegamos a la 'Z', el conteo vuelva a empezar desde la 'A'
    nueva_posicion = (posicion + desplazamiento) % 26
    return abc[nueva_posicion]

# Función para procesar el mensaje completo
def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    # Recorremos cada carácter del mensaje original
    for caracter in mensaje:
        # Verificamos si es una letra válida (A-Z)
        if "A" <= caracter.upper() <= "Z":
            resultado += cifrar_letra(caracter, desplazamiento)
        else:
            # Si es un espacio o puntuación, se añade sin cambios
            resultado += caracter 
    return resultado

# --- Lógica principal del programa ---
print("--- BIENVENIDO AL CIFRADOR CÉSAR ---")

# Pedimos el texto al usuario
texto_usuario = input("Introduce el mensaje que quieres cifrar: ")

# Bucle para validar que el desplazamiento sea un número entre 1 y 25
desplazamiento = 0
while desplazamiento < 1 or desplazamiento > 25:
    try:
        desplazamiento = int(input("Introduce el desplazamiento (1-25): "))
        if desplazamiento < 1 or desplazamiento > 25:
            print("¡Error! Debe ser un número entre 1 y 25.")
    except ValueError:
        # Manejamos el error si el usuario introduce texto en lugar de un número
        print("Por favor, introduce un número válido.")

# Llamamos a la función principal y mostramos el resultado
mensaje_cifrado = cifrar_mensaje(texto_usuario, desplazamiento)
print(f"\n Mensaje cifrado: {mensaje_cifrado}")