def generarUsuarios(usuarios):
	if usuarios:
		usuarios.clear()
	dni = [41587459, 40902958, 42302303, 24748234, 31933841]
	pin = ["1010", "1515", "4545", "7423", "1238"]
	nomApe = ["camilo_fabregas", "agustina_manduca", "mariano_fortunato", "damian_gomez", "marta_diaz"]
	celular = ["1122503503", "1184623564", "1551418306", "1162846123", "1186847247"]
	for dato1, dato2, dato3, dato4 in zip(dni, pin, nomApe, celular):
		usuarios[dato1] = [dato2, dato3, dato4]

def generarBicicletas(bicicletas):
	for num in range(1000,1240):
		bicicletas[num] = ["En condiciones", "Anclada en estación"]
	for num in range(1240,1250):
		bicicletas[num] = ["Necesita reparación", "En reparación"]

def generarEstaciones(estaciones, bicicletas, tipoDeCarga):
	if estaciones:
		estaciones.clear()
	identificador = list(range(1,11))
	direcciones = ["Parque Lezama", "Plaza de Mayo", "Retiro", "Facultad de Derecho", "Obelisco", "Congreso", "Constitución", "Planetario", "Parque Centenario", "Alto Palermo"]
	latitudLongitud = [(-34.6261, -58.3684), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.5828, -58.3920), (-34.6037, -58.3814), (-34.6095, -58.3889), (-34.6266, -58.3811), (-34.5696, -58.4117), (-34.6073, -58.4335), (-34.5890, -58.4100)]
	anclajesTotales = [30, 25, 20, 30, 30, 25, 30, 15, 25, 25]
	anclajesOcupados = distribuirBicicletas(anclajesTotales, tipoDeCarga)
	for dato1, dato2, dato3, dato4, dato5 in zip(identificador, direcciones, latitudLongitud, anclajesTotales, anclajesOcupados):
		estaciones[dato1] = {"Dirección": dato2, "Latitud y longitud": dato3, "Capacidad": dato4, "Bicicletas": dato5}

def distribuirBicicletas(anclajes, tipoDeCarga):
	if tipoDeCarga == "predefinida":
		distribucionAnclajes = [22, 15, 27, 24, 22, 29, 24, 28, 19, 30]
		idBicis = list(range(1000, 1240))
		resultadoFinal = []
		for i in distribucionAnclajes:
			resultadoParcial = {}
			bicisPorEstacion = [x for x in idBicis if idBicis.index(x) < i]
			for bici in bicisPorEstacion:
				idBicis.remove(bici)
				resultadoParcial[bicisPorEstacion.index(bici)+1] = bici
			resultadoFinal.append(resultadoParcial)
		return resultadoFinal
	else:
		print("CARGA ALEATORIA")
		distribucionBicicletas = ["asdasdasdasd"]
		return distribucionBicicletas
