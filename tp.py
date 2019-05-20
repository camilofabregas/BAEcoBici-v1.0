from imprimirMenus import *
from generarEstructuras import *
from validaciones import *
import random

def main():
	usuarios, bicicletas, estaciones = dict(), dict(), dict() # Defino los diccionarios vacíos.
	imprimirLogo() # En el módulo menuYSubmenus
	menuPrincipal(usuarios, bicicletas, estaciones)


def menuPrincipal(usuarios, bicicletas, estaciones):
	opcionElegida = 0
	while opcionElegida != 6:
		imprimirMenuPrincipal() # En el módulo menuYSubmenus
		opcionElegida = ingresarEntreRangos(1,6,"[SOLICITUD] Ingrese el número de opción (1 a 6): ")
		submenuElegido(opcionElegida, usuarios, bicicletas, estaciones)

def ingresarEntreRangos(inicio, fin, mensaje): #Para ingresar (y validar) una opción dentro de un rango especifico.
	opcion = input(mensaje)
	while not opcion.isdigit() or int(opcion) < inicio or int(opcion) > fin:
		print("\n[ERROR] Debe estar dentro del rango especificado.")
		opcion = input(mensaje)
	return int(opcion)

def submenuElegido(opcionElegida, usuarios, bicicletas, estaciones): # Genera el submenu de la opción que elegí en el menu principal
	if opcionElegida != 5 and opcionElegida != 6: # Si no es "Salir del programa" o "Ingresar al sistema"
		rangoSubmenuElegido = calcularRangoSubmenuElegido(opcionElegida)
		opcionSubmenu = 0
		while opcionSubmenu != rangoSubmenuElegido:
			imprimirSubmenuElegido(opcionElegida) # En el módulo menuYSubmenus
			opcionSubmenu = ingresarEntreRangos(1,rangoSubmenuElegido,"Ingrese el número de opción (1 a {}): ".format(rangoSubmenuElegido))
			invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones)
	elif opcionElegida == 5:
		menuUsuario(usuarios)

def calcularRangoSubmenuElegido(opcionElegida):
	if opcionElegida == 1 or opcionElegida == 3:
		return 3
	elif opcionElegida == 2:
		return 5
	elif opcionElegida == 4:
		return 4

def invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones):
	if opcionElegida == 1 and opcionSubmenu == 1:
		cargarDatos(usuarios, bicicletas, estaciones, "predefinida")
	elif opcionElegida == 1 and opcionSubmenu == 2:
		cargarDatos(usuarios, bicicletas, estaciones, "aleatoria") # Idem pero cambia la distribución de bicicletas.
	elif opcionElegida == 2 and opcionSubmenu == 1:
		listado()
	elif opcionElegida == 2 and opcionSubmenu == 2:
		alta(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 3:
		modificacion(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 4:
		desbloquear()
	elif opcionElegida == 3 and opcionSubmenu == 1:
		viajeAleatorio()
	elif opcionElegida == 3 and opcionSubmenu == 2:
		viajesAleatoriosMultiples()
	elif opcionElegida == 4 and opcionSubmenu == 1:
		topUsuariosCantidadViajes()
	elif opcionElegida == 4 and opcionSubmenu == 2:
		topUsuariosDuracionViajes()
	elif opcionElegida == 4 and opcionSubmenu == 3:
		bicicletasEnReparacion()
	elif opcionElegida == 4 and opcionSubmenu == 4:
		estacionesMasActivas()

def cargarDatos(usuarios, bicicletas, estaciones, tipoDeCarga):
	generarUsuarios(usuarios) # En el módulo generarEstructuras
	generarBicicletas(bicicletas) # En el módulo generarEstructuras
	generarEstaciones(estaciones, bicicletas, tipoDeCarga) # En el módulo generarEstructuras
	print("\n\n[INFO] Se ha realizado una carga automática {} de datos de usuarios, bicicletas y estaciones.\nVolviendo al submenú de carga de datos...".format(tipoDeCarga))

def alta(usuarios):
	print(usuarios)
	dni = int(solicitarValidarDigitos(7, 8, "[SOLICITUD] Ingrese su DNI (sin puntos ni espacios): "))
	if dni not in usuarios:
		pin = solicitarValidarDigitos(4, 4, "[SOLICITUD] Ingrese un PIN de 4 dígitos: ")
		nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
		apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
		celular = solicitarValidarCelular()
		usuarios[dni] = [pin, nombre + "_" + apellido, celular] 
		return usuarios
	else:
		print("\n\n[ERROR] El DNI ingresado ya se asociado a una cuenta en el sistema. Volviendo al menú principal...")

def modificacion (usuarios):
	opcionElegida = 0 
	while opcionElegida != 5:
		imprimirMenuModificacion()
		opcionElegida = ingresarEntreRangos(1, 5, "[SOLICITUD] Ingrese el número de opción (1 a 5): ")
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
					print ("[INFO] Nombre y apellido del usuario {} fue cambiado con éxito.".format(dni))
				elif opcionElegida == 3:
					celular = solicitarValidarCelular()
					usuarios [dni][2] = celular
					print ("[INFO] Celular del usuario {} cambiado con exito.".format(dni))
				elif opcionElegida == 4:
					confirmacion = input("El usuario de DNI {} será eliminado. ¿Desea confirmar? s/n: ".format(dni))
					if confirmacion == "s":
						del usuarios[dni]
						print("[INFO] El usuario {} fue eliminado con éxito.".format(dni))
					else:
						print ("[INFO] Operacion cancelada. Volviendo al menu de modificación...\n")
			else:
				print ("[ERROR] El DNI ingresado no se encuentra en el sistema. Volviendo al menu de modificación... \n")

def menuUsuario(usuarios):
	dni, pin = iniciarSesion(usuarios) 
	if dni != 0:
		opcionElegida = 0
		while opcionElegida != 4:
			imprimirMenuUsuario()
			opcionElegida = ingresarEntreRangos(1,4,"[SOLICITUD] Ingrese el número de opción (1 a 4): ")
			submenuUsuario(usuarios, opcionElegida, dni, pin)

def iniciarSesion(usuarios):
	print("\n\n**** INICIAR SESIÓN *****")
	dni = input("[SOLICITUD] Ingrese su DNI: ")
	if dni.isdigit() and int(dni) in usuarios:
		pin = input("[SOLICITUD] Ingrese su PIN asociado: ")
		while pin != usuarios[int(dni)][0]:
			pin = input("[ERROR] PIN incorrecto, pruebe de nuevo.\nIngrese su PIN asociado: ")
		return int(dni), pin
	else:
		print("[ERROR] No hay una cuenta registrada con ese DNI, volviendo al menu principal...")
		return 0, 0

def submenuUsuario(usuarios, opcionElegida, dni, pin):
	if opcionElegida == 1:
		cambiarPin(usuarios, dni, pin)
	elif opcionElegida == 2:
		retirarBicicleta()
	elif opcionElegida == 3:
		devolverBicicleta()

def cambiarPin(usuarios, dni, pinViejo):
	print("\n")
	pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
	while pinNuevo == pinViejo:
		print("\n[ERROR] El PIN ingresado ya está asociado a su cuenta.")
		pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
	pinNuevoRepetido = solicitarValidarDigitos(4, 4,"\n[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
	while pinNuevo != pinNuevoRepetido:
		print("\n[ERROR] Los pines no coinciden, intente de nuevo...")
		pinNuevoRepetido = solicitarValidarDigitos(4, 4,"\n[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
	usuarios[dni][0] = pinNuevo
	print("[INFO] El PIN fue cambiado con éxito.")


main()
