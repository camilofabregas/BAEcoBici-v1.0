import random

def generarUsuarios(usuarios):
	if usuarios:
		usuarios.clear()
	dni = ["41587459", "17199330", "17331253", "24748234", "31933841"]
	pin = ["1010", "8491", "1010", "7423", "1238"]
	nomApe = ["camilo_fabregas", "ignacio_sanchez", "carla_martinez", "damian_gomez", "marta_diaz"]
	celular = ["1122503503", "1184623564", "1573861543", "1162846123", "1186847247"]
	for dato1, dato2, dato3, dato4 in zip(dni, pin, nomApe, celular):
		usuarios[dato1] = [dato2, dato3, dato4]

def generarBicicletas(bicicletas):
	for num in range(1000,1241):
		bicicletas[num] = ["En condiciones", "Anclada en estación"]
	for num in range(1241,1251):
		bicicletas[num] = ["Necesita reparación", "En reparación"]

def cargaAutomaticaAleatoria(usuarios, bicicletas, estaciones):
    generarUsuarios(usuarios)
    generarBicicletas(bicicletas)
    generarEstacionesRandom(estaciones, bicicletas)

def generarEstacionesRandom(estaciones, bicicletas):
    identificador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    direcciones = ["Parque Lezama", "Plaza de Mayo", "Retiro", "Facultad de Derecho", "Obelisco", "Congreso", "Constitución", "Parque Patricios", "Planetario", "Parque Centenario", "Alto Palermo"]
    latitudLongitud = [(-34.6261, -58.3684), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.5828, -58.3920), (-34.6037, -58.3814), (-34.6095, -58.3889), (-34.6266, -58.3811), (-34.6385, -58.4060), (-34.5717, -58.4112), (-34.6073, -58.4335), (-34.5890, -58.4100)]
    capacidad = [30, 25, 20, 30, 30, 25, 30, 15, 25, 30, 25]
    for dato1, dato2, dato3, dato4 in zip(identificador, direcciones, latitudLongitud, capacidad):
    	estaciones[dato1] = {"Dirección": dato2, "Latitud y longitud": dato3, "Capacidad": dato4, "Anclajes":[]}

    bicis = list(bicicletas.keys())
    while len(bicis) > 0:
        for idEstacion in estaciones:
            numAnclajes = len(estaciones[idEstacion]["Anclajes"])
            capacidad = estaciones[idEstacion]["Capacidad"]
            if numAnclajes != capacidad:
                anclajesAsignados = random.randrange(capacidad - numAnclajes)
                for anclaje in range(anclajesAsignados):
                    biciAsignada = random.randrange(len(bicis))
                    estaciones[idEstacion]["Anclajes"].append(bicis[biciAsignada])
                    del(bicis[biciAsignada])

usuarios, bicicletas, estaciones = dict(), dict(), dict()
cargaAutomaticaAleatoria(usuarios, bicicletas, estaciones)
print(estaciones)