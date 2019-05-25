from datetime import time

def topUsuariosDuracionViajes(viajesFinalizados):
	usuariosMasDuracion = {}
	for dni in viajesFinalizados:
		duracionHora = 0
		duracionMin = 0
		duracionSeg = 0
		for viaje in range(len(viajesFinalizados[dni])):
			salida = viajesFinalizados[dni][viaje][2]
			llegada = viajesFinalizados[dni][viaje][4]
			diferenciaHora = abs((llegada.hour - salida.hour))
			diferenciaMinutos = abs((llegada.minute - salida.minute))
			diferenciaSegundos = abs((llegada.second - salida.second))
			duracionHora += diferenciaHora
			duracionMin += diferenciaMinutos
			duracionSeg += diferenciaSegundos
			if duracionSeg >= 60:
				duracionMin += 1
				duracionSeg = duracionSeg - 60
			if duracionMin >= 60:
				duracionHora += 1
				duracionMin = duracionMin - 60
		duracion = time(duracionHora, duracionMin, duracionSeg)
		if dni not in usuariosMasDuracion:
			usuariosMasDuracion[dni] = duracion
		else:
			sumaSegundos = (usuariosMasDuracion[dni].second + duracion.second)
			if sumaSegundos >= 60:
				sumaMinutos = (usuariosMasDuracion[dni].minute + duracion.minute) + 1
				sumaSegundos = sumaSegundos - 60
			else:
				sumaMinutos = (usuariosMasDuracion[dni].minute + duracion.minute)
			if sumaMinutos >= 60:
				sumaHoras = (usuariosMasDuracion[dni].hour + duracion.hour)
				sumaMinutos = sumaMinutos - 60
			else: 
				sumaHoras = (usuariosMasDuracion[dni].hour + duracion.hour)
			usuariosMasDuracion[dni] = time(sumaHoras, sumaMinutos, sumaSegundos)
	print("\n**** USUARIOS CON MAYOR TIEMPO DE VIAJE ****\n")
	topOrdenado = sorted(usuariosMasDuracion.items(), key = lambda x: x[1], reverse = True)
	contador = 1
	for usuarios in topOrdenado:
		print(contador,". Usuario {} con {} hs de viaje.".format(usuarios[0], usuarios[1]))
		contador +=1
