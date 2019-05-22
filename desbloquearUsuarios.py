import random

def imprimirUsuariosBloqueados (usuarios):
    cantidadUsuariosBloqueados = 0 #Indice para imprimir ordenado
    print("**** Usuarios Bloqueados ****")
    for usuario in usuarios:
        if usuarios[usuario][0] == "": #Filtro del diccionario los usarios bloqueados
            cantidadUsuariosBloqueados += 1
            print("{}. {} con dni {}".format(cantidadUsuariosBloqueados, usuarios[usuario][1], usuario)) #imprimo indice, nombre de usuario y dni
    return cantidadUsuariosBloqueados

def generarPin():
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    num3 = random.choice('0123456789')
    num4 = random.choice('0123456789')
    nuevoPin = num + num2 + num3 + num4 
    return nuevoPin

def desbloquear (usuarios):
    cantidadUsuariosBloqueados = imprimirUsuariosBloqueados(usuarios)
    if cantidadUsuariosBloqueados > 0:
        clave = input("Ingrese palabra secreta de desbloqueo: ")
        if clave == "shimano":
            usuarioElegido = input("Ingrese el DNI del usuario a desbloquear: ")
            while usuarioElegido not in usuarios or usuarios[usuarioElegido][0] != "":
                usuarioElegido = input("[ERROR] Debe ingresar el DNI de un usuario bloqueado: ")
            usuarios[usuarioElegido][0] = generarPin()
            print("[INFO] Usuario desbloqueado exitosamente. Se le generó el pin {}, a {}.".format(usuarios[usuarioElegido][0], usuarios[usuarioElegido][1]))
        else:
            print("[ERROR] Palabra incorrecta")
    else:
        print("No hay usuarios bloqueados")
    print("[INFO] Volviendo al submenu...")