import random

def generarUsuarios():
    dni = [41587459, 17199330, 17331253, 24748234, 31933841]
    pin = ["-", "8491", "-", "7423", "-"]
    nomApe = ["camilo_fabregas", "ignacio_sanchez", "carla_martinez", "damian_gomez", "marta_diaz"]
    celular = ["1122503503", "1184623564", "1573861543", "1162846123", "1186847247"]
    usuarios = {}
    for dato1, dato2, dato3, dato4 in zip(dni, pin, nomApe, celular):
        usuarios[dato1] = [dato2, dato3, dato4]
    return usuarios


def imprimirUsuariosBloqueados (usuarios):
    cantidadUsuariosBloqueados = 0 #Indice para imprimir ordenado
    seguir = "s"
    print("**** Usuarios Bloqueados ****")
    for usuario in usuarios:
        if usuarios[usuario][0] == "-": #Filtro del diccionario los usarios bloqueados
            cantidadUsuariosBloqueados += 1
            print("{}. {}".format(cantidadUsuariosBloqueados, usuarios[usuario][1])) #imprimo indice, nombre de usuario
    return cantidadUsuariosBloqueados

def generarPin():
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    num3 = random.choice('0123456789')
    num4 = random.choice('0123456789')
    nuevoPin = num + num2 + num3 + num4 
    return nuevoPin

def desbloquear (usuarios, cantidadUsuariosBloqueados, nuevoPin):
    seguir = "s"
    while seguir == "s":
        usuarioElegido = int(input("Ingrese el DNI del usuario a desbloquear: "))
        while usuarioElegido not in usuarios:
            usuarioElegido = int(input("[ERROR] Debe ingresar el DNI de un usuario bloqueado: "))
        for dni in usuarios:
            if dni == usuarioElegido and usuarios[dni][0] == "-":
                usuarios[dni][0] = nuevoPin
                print("[INFO] Usuario desbloqueado exitosamente. Se le generó el pin {}, a {}.".format(nuevoPin, usuarios[dni][1]))
        seguir = input('¿Desea desbloquear otro usuario? (s/n): ')
    print("[INFO] Volviendo al submenu...")

usuarios = generarUsuarios()
imprimir = imprimirUsuariosBloqueados(usuarios)
nuevoPin = generarPin()
desbloquear(usuarios, imprimir, nuevoPin)
