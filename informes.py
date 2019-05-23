def bicicletasEnReparacion (bicicletas, estaciones):
	bicisEnReparacion = []
	for bicicleta in bicicletas:
		if bicicletas[bicicleta][0] == "Necesita reparación":
			bicisEnReparacion.append(bicicleta)
	for bicicleta in bicisEnReparacion:
		estacionBici = random.randrange(1, len(estaciones)+1)
		print("[INFO] La bicicleta {} ubicada en la estacion {} necesita reparacion. ".format(bicicleta, estaciones[estacionBici]["Dirección"]))

