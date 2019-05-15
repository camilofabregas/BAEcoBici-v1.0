def generarUsuarios():
	dni = [41587459, 17199330, 17331253, 24748234, 31933841]
	pin = [1010, 8491, 1010, 7423, 1238]
	nomApe = ["camilo_fabregas", "ignacio_sanchez", "carla_martinez", "damian_gomez", "marta_diaz"]
	celular = ["1122503503", "1184623564", "1573861543", "1162846123", "1186847247"]
	usuarios = {}
	for dato1, dato2, dato3, dato4 in zip(dni, pin, nomApe, celular):
		usuarios[dato1] = [int(dato2), dato3, dato4]
	return usuarios

def generarBicicletas():
	bicicletas = {}
	for num in range(1,241):
		bicicletas[num] = ["En condiciones", "Anclada en estación"]
	for num in range(241,251):
		bicicletas[num] = ["Necesita reparación", "En reparación"]
	return bicicletas


def generarEstaciones():
	direcciones = ["Parque Lezama", "Plaza de Mayo", "Retiro", "Facultad de Derecho", "Obelisco", "Congreso", "Constitución", "Parque Patricios", "Planetario", "Parque Centenario", "Alto Palermo"]
	latitudLongitud = [(-34.6261, -58.3684), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.5828, -58.3920), (-34.6037, -58.3814), (-34.6095, -58.3889), (-34.6266, -58.3811), (-34.6385, -58.4060), (-34.5717, -58.4112), (-34.6073, -58.4335), (-34.5890, -58.4100)]
	anclajesTotales = [30, 25, 20, 30, 30, 25, 30, 15, 25, 30, 25]
	anclajesOcupados = [25, 20, 20, 25, 25, 20, 20, 15, 20, 30, 20]
	estaciones = {}
	for num in range(1,11): # Rango de identificador de la estación
		for dato1, dato2, dato3, dato4 in zip(direcciones, latitudLongitud, anclajesTotales, anclajesOcupados):
			estaciones[num] = {"Dirección": dato1, "Latitud y longitud": dato2, "Capacidad": dato3, "Bicicletas": dato4}
	return estaciones

