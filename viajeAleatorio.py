def viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
	usuariosDisponibles = [usuario for usuario in usuarios if usuarios[usuario][0] != "" and usuario not in usuariosEnViaje]
	if usuariosDisponibles:
		usuario = random.choice(usuariosDisponibles)
		estacionRetirar, bicicletaAsignada = retiroAleatorioBicicleta(estaciones, bicicletas)
		horarioSalida = horarios(0, 0, 0, 23, 30, 60)
		print("\n{} retiró la bicicleta {} de la estación N°{} de {} a las {}:{}:{}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionRetirar, estaciones[estacionRetirar]["Dirección"], horarioSalida[0], horarioSalida[1], horarioSalida[2]))
		estacionDevolver = devolucionAleatoriaBicicleta(estaciones, bicicletaAsignada, estacionRetirar)
		duracionViaje = horarios(0, 0, 0, 2, 30, 60)  # maximo 90 minutos que equivale a 1:30:00hs
		horarioLlegada = calcularHoraLlegada(horarioSalida, duracionViaje)
		print("{} devolvió la bicicleta {} en la estación N°{} de {} a las {}:{}:{}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionDevolver, estaciones[estacionDevolver]["Dirección"], horarioLlegada[0], horarioLlegada[1], horarioLlegada[2]))
		bloqueoExcesoHorario(usuarios, duracionViaje, usuario)
		acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada)
	else:
		return "None"

def retiroAleatorioBicicleta(estaciones, bicicletas):
    bicicletaAsignada = ""
    while not bicicletaAsignada:
        estacionRetirar = random.randrange(1, 11)
        for anclaje in estaciones[estacionRetirar]["Bicicletas"]:
            bici = estaciones[estacionRetirar]["Bicicletas"][anclaje]
            if bici and bicicletas[bici][0] != "Necesita reparación":
                estaciones[estacionRetirar]["Bicicletas"][anclaje] = ""
                return estacionRetirar, bici

def devolucionAleatoriaBicicleta(estaciones, bici, estacionRetirar):
    estacionDevolver = estacionRetirar
    while estacionDevolver == estacionRetirar:
        estacion = random.randrange(1, 11)
        for anclaje in estaciones[estacion]["Bicicletas"]:
            if estaciones[estacion]["Bicicletas"][anclaje] == "":
                estaciones[estacion]["Bicicletas"][anclaje] = bici
                return estacion

def bloqueoExcesoHorario(usuarios, duracionViaje, usuario):
    if duracionViaje[0] == 1 and duracionViaje[1] >= 0:
        usuarios[usuario][0] = ""
        print("Al exceder los 60 minutos de uso ha sido bloqueado")

def acumularViajes(usuario, viajesFinalizados, bicicletaAsignada, estacionRetirar, estacionDevolver, horarioSalida, horarioLlegada):
    if usuario not in viajesFinalizados:
        viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2]), estacionDevolver,str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2]))]
    else:
        viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2]), estacionDevolver, str(horarioLlegada[0])+":"+str(horarioLlegada[1])+":"+str(horarioLlegada[2])))

def viajesAleatoriosMultiples(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
	cantidad = ingresarEntreRangos(1, 100, "Ingrese entre 1 y 100 la cantidad de viajes aleatorios que desea generar: ")
	for viaje in range(cantidad-1):
		viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados)
		if viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados) == "None":
			return print("[INFO] No hay mas usuarios disponibles. Se encuentran todos en viaje o bloqueados.")

def calcularHoraLlegada(horarioSalida, duracionViaje):
	horaLlegada = horarioSalida[0] + duracionViaje[0]
	minLlegada = horarioSalida[1] + duracionViaje[1]
	segLlegada = horarioSalida[2] + duracionViaje[2]
	if segLlegada >= 60:
		segLlegada = segLlegada - 60
		minLlegada += 1
	if minLlegada >= 60:
		minLlegada = minLlegada - 60
		horaLlegada +=1
	return (horaLlegada, minLlegada, segLlegada)
