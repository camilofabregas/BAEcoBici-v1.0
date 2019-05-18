def modificacion (usuarios):
	opcionElegida = 0 
	while opcionElegida != 5:
		print ("\n\n**** MODIFICACION DE DATOS ****\n1. Modificacion de PIN\n2. Modifiacion de Nombre y apellido\n3. Modificacion de celular\n4. Eliminar usuario\n5. Volver al menu anterior\n")
		opcionElegida = ingresarEntreRangos(1, 5, "Ingrese el número de opción (1 a 5): ")
		if opcionElegida != 5:
			dni = input("[SOLICITUD] Ingrese el DNI: ")
			if dni.isdigit() and int(dni) in usuarios:
				dni = int(dni)
				if opcionElegida == 1:
					pin = input("[SOLICITUD] Ingrese el PIN asociado: ")
					cambiarPin(usuarios, dni, pin)
				elif opcionElegida == 2:
					nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
					apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
					usuarios[dni][1] = nombre + "_" + apellido
					print ("[INFO] Nombre y apellido del usuario {} fue cambiado con exito.".format(dni))
				elif opcionElegida == 3:
					celular = solicitarValidarCelular()
					usuarios [dni][2] = celular
					print ("[INFO] Celular del usuario {} cambiado con exito.".format(dni))
				elif opcionElegida == 4:
					confirmacion = input("El usuario de DNI {} sera eliminado. Desea confirmar? s/n: ".format(dni))
					if confirmacion == "s":
						del usuarios[dni]
						print("[INFO] El usuario {} fue eliminado con exito.".format(dni))
					else:
						print ("[INFO] Operacion cancelada. Volviendo al menu de modificacion...\n")
			else:
				print ("El DNI ingresado no se encuentra en el sistema. Volviendo al menu de modificacion... \n")
		print(usuarios)
"""				
def modificacionNombreApe (usuarios, dni):
	nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
	apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
	usuarios[dni][1] = nombre + "_" + apellido
	print ("[INFO] Nombre y apellido del usuario {} cambiado con exito.".format(dni))

def modificacionCelular (usuarios, dni):
	celular = solicitarValidarCelular()
	print ("[INFO] Celular del usuario {} cambiado con exito.".format(dni))
"""