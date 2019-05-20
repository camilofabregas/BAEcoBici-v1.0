def generarUsuarios(usuarios):
	if usuarios:
		usuarios.clear()
	dni = [41587459, 17199330, 17331253, 24748234, 31933841]
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

def generarEstaciones(estaciones, bicicletas, tipoDeCarga):
	if estaciones:
		estaciones.clear()
	identificador = list(range(1,11))
	direcciones = ["Parque Lezama", "Plaza de Mayo", "Retiro", "Facultad de Derecho", "Obelisco", "Congreso", "Constitución", "Planetario", "Parque Centenario", "Alto Palermo"]
	latitudLongitud = [(-34.6261, -58.3684), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.5828, -58.3920), (-34.6037, -58.3814), (-34.6095, -58.3889), (-34.6266, -58.3811), (-34.5696, -58.4117), (-34.6073, -58.4335), (-34.5890, -58.4100)]
	anclajesTotales = [30, 25, 20, 30, 30, 25, 30, 15, 25, 25]
	anclajesOcupados = distribuirBicicletas(bicicletas, tipoDeCarga)
	for dato1, dato2, dato3, dato4, dato5 in zip(identificador, direcciones, latitudLongitud, anclajesTotales, anclajesOcupados):
		estaciones[dato1] = {"Dirección": dato2, "Latitud y longitud": dato3, "Capacidad": dato4, "Bicicletas": dato5}

def distribuirBicicletas(bicicletas, tipoDeCarga):
	if tipoDeCarga == "predefinida":
		print("CARGA PREDEFINIDA")
		distribucionBicicletas = [list(range(1000, 1030)), list(range(1030,1055)), list(range(1055,1075)), list(range(1075,1105)), list(range(1105,1135)), list(range(1135,1160)), list(range(1160,1190)), list(range(1190,1205)), list(range(1205,1230)), list(range(1230,1251))]
		return distribucionBicicletas
	else:
		print("CARGA ALEATORIA")
		distribucionBicicletas = ["asdasdasdasd"]
		return distribucionBicicletas
