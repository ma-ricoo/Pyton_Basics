def cifrar_letra(letra, desplazamiento):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posicion = abc.find(letra.upper())
    
    if posicion == -1: 
        return letra
        
    nueva_posicion = (posicion + desplazamiento) % 26
    return abc[nueva_posicion]

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if "A" <= caracter.upper() <= "Z":
            resultado += cifrar_letra(caracter, desplazamiento)
        else:
            resultado += caracter 
    return resultado



print("--- BIENVENIDO AL CIFRADOR CÉSAR ---")


texto_usuario = input("Introduce el mensaje que quieres cifrar: ")


desplazamiento = 0
while desplazamiento < 1 or desplazamiento > 25:
    try:
        desplazamiento = int(input("Introduce el desplazamiento (1-25): "))
        if desplazamiento < 1 or desplazamiento > 25:
            print("¡Error! Debe ser un número entre 1 y 25.")
    except ValueError:
        print("Por favor, introduce un número válido.")

mensaje_cifrado = cifrar_mensaje(texto_usuario, desplazamiento)
print(f"\n Mensaje cifrado: {mensaje_cifrado}")
