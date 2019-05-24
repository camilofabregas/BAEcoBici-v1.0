def topUsuariosDuracionViajes(viajesFinalizados):
	usuariosMasDuracion = {}
	for dni in viajesFinalizados:
		salida = viajesFinalizados[dni][0][2]
		llegada = viajesFinalizados[dni][0][4]
		diferenciaHora = abs((llegada.hour - salida.hour))
		diferenciaMinutos = abs((llegada.minute - salida.minute))
		diferenciaSegundos =abs((llegada.second - salida.second))
		if dni not in usuariosMasDuracion:
			usuariosMasDuracion[dni] = time(diferenciaHora,diferenciaMinutos,diferenciaSegundos)
		else:
			sumaSegundos = (usuariosMasDuracion[dni].second + diferenciaSegundos)
			if sumaSegundos >= 60:
				sumaMinutos = (usuariosMasDuracion[dni].minute + diferenciaMinutos) + 1
				sumaSegundos = sumaSegundos - 60
			else:
				sumaMinutos = (usuariosMasDuracion[dni].minute + diferenciaMinutos)
			if sumaMinutos >= 60:
				sumaHoras = (usuariosMasDuracion[dni].hour + diferenciaHora)
				sumaMinutos = sumaMinutos - 60
			else: 
				sumaHoras = (usuariosMasDuracion[dni].hour + diferenciaHora)
			usuariosMasDuracion[dni] = time(sumaHoras, sumaMinutos, sumaSegundos)
	print("\n**** USUARIOS CON MAYOR TIEMPO DE VIAJE ****\n")
	topOrdenado = sorted(usuariosMasDuracion.items(), key = lambda x: x[1], reverse = True)
	contador = 1
	for usuarios in topOrdenado:
		print(contador,". Usuario {} con {} hs de viaje.".format(usuarios[0], usuarios[1]))
		contador +=1