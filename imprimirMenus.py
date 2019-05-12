def imprimirMenuPrincipal():
	print("\n\n***** MENU PRINCIPAL *****")
	print("\n1. Carga de datos")#\n**** a. Carga automática\n**** b. Carga automática aleatoria")
	print("2. Usuarios")#\n**** a. Listado\n**** b. Alta\n**** c. Modificación\n**** d. Desbloquear")
	print("3. Retiros automáticos")#\n**** a. Viaje aleatorio\n**** b. Viajes aleatorios múltiples")
	print("4. Informes")#\n**** a. Usuarios con mayor cantidad de viajes\n**** b. Usuarios con mayor duración acumulada de viajes\n**** c. Bicicletas en reparación\n**** d. Estaciones más activas")
	print("5. Ingresar al sistema")
	print("6. Salir del programa")

def imprimirLogo():
	print("\n**************************************")
	print("***                                ***")
	print("***         BAEcoBici v1.0         ***")
	print("***                                ***")
	print("**************************************")

def imprimirSubmenuElegido(opcionElegida):
	if opcionElegida == 1:
		print("\n\n**** CARGA DE DATOS ****\n    1. Carga automática\n    2. Carga automática aleatoria\n    3. Volver al menu principal")
	elif opcionElegida == 2:
		print("\n\n**** USUARIOS ****\n    1. Listado\n    2. Alta\n    3. Modificación\n    4. Desbloquear\n    5. Volver al menu principal")
	elif opcionElegida == 3:
		print("\n\n**** RETIROS AUTOMÁTICOS ****\n    1. Viaje aleatorio\n    2. Viajes aleatorios múltiples\n    3. Volver al menu principal")
	elif opcionElegida == 4:
		print("\n\n**** INFORMES ****\n    1. Usuarios con mayor cantidad de viajes\n    2. Usuarios con mayor duración acumulada de viajes\n    3. Bicicletas en reparación\n    4. Estaciones más activas\n    5. Volver al menu principal")
