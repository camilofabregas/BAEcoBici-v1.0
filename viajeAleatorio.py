import random
from datetime import time

def viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
    usuario = random.choice(list(usuarios.keys()))
    while usuarios[usuario][0] == "" or usuario in usuariosEnViaje:
        usuario = random.choice(list(usuarios.keys()))
    estacionRetirar = random.randrange(1, 11)
    while len(estaciones[estacionRetirar]["Bicicletas"]) == 0:
        estacionRetirar = random.randrange(1, 11)
    anclajesDisponibles = list(estaciones[estacionRetirar]["Bicicletas"].keys())
    anclajeAsignado = random.choice(anclajesDisponibles)
    bicicletaAsignada = estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
    while bicicletas[bicicletaAsignada] == ["Necesita reparación", "En reparación"]:
        anclajeAsignado = random.randrange(1, len(estaciones[estacionRetirar]["Bicicletas"])+1)
        bicicletaAsignada = estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
    del estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
    horaSalida, minSalida, segSalida = horarios(0, 0, 0, 23, 60, 60)
    while horaSalida == 22 and minSalida > 29:
        horaSalida, minSalida, segSalida = horarios(0, 0, 0, 23, 60, 60)
    print("\n{} retiró la bicicleta {} de la estación N°{} de {} a las {}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionRetirar, estaciones[estacionRetirar]["Dirección"], time(horaSalida, minSalida, segSalida)))
    estacionDevolver = random.randrange(1, 11)
    while estacionDevolver == estacionRetirar or len(estaciones[estacionDevolver]["Bicicletas"]) == estaciones[estacionDevolver]["Capacidad"]:
        estacionDevolver = random.randrange(1, 11)
    horaViaje, minViaje, segViaje = horarios(0, 0, 0, 2, 30, 60)  # maximo 90 minutos que equivale a 1:30:00hs
    horaLlegada, minLlegada, segLlegada = calcularHoraLlegada(horaSalida, minSalida, segSalida, horaViaje, minViaje, segViaje)
    print("{} devolvió la bicicleta {} en la estación N°{} de {} a las {}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionDevolver, estaciones[estacionDevolver]["Dirección"], time(horaLlegada, minLlegada, segLlegada)))
    if horaViaje == 1 and segViaje > 0:
        usuarios[usuario][0] = ""
        print("Al exceder los 60 minutos de uso ha sido bloqueado")
    if usuario not in viajesFinalizados:
        viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada))]
    elif usuario in viajesFinalizados:  # acumula los viajes de un mismo usuario
        viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida) , estacionDevolver, time(horaLlegada, minLlegada, segLlegada)))  # no me funciona el time()
    
    print("\nDICCIONARIOS")
    print(viajesFinalizados)  # para verificar
    print(usuarios)  # para verificar si bloquea el usuario al exceder tiempo

def calcularHoraLlegada(horas, minutos, segundos, horaViaje, minViaje, segViaje):
    horaLlegada = horas + horaViaje
    minLlegada = minutos + minViaje
    segLlegada = segundos + segViaje
    if segLlegada >= 60:
        segLlegada = segLlegada - 60
        minLlegada += 1
    if minLlegada >= 60:
        minLlegada = minLlegada - 60
        horaLlegada +=1
    return (horaLlegada, minLlegada, segLlegada)

def horarios (horaMinimo, minutosMinimo, segundosMinimo, horaMaximo, minutosMaximo, segundosMaximo):
	horas = random.randrange(horaMinimo, horaMaximo)
	minutos = random.randrange(minutosMinimo, minutosMaximo)
	segundos = random.randrange(segundosMinimo, segundosMaximo)
	return (horas, minutos, segundos)

# USO FUNCIONES QUE YA ESTAN EN TP, PERO LAS IMPORTO DESDE ACA PARA NO METERLO DE UNA Y PARA QUE PRUEBEN ANTES
# DEBERIAN AGREGAR A TP: from viajeAleatorio import *
