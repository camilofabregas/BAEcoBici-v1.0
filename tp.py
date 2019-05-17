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
		opcionElegida = ingresarEntreRangos(1,6,"Ingrese el número de opción (1 a 6): ")
		submenuElegido(opcionElegida, usuarios, bicicletas, estaciones)

def ingresarEntreRangos(inicio, fin, mensaje): #Para ingresar (y validar) una opción dentro de un rango especifico.
	opcion = input(mensaje)
	while not opcion.isdigit() or int(opcion) < inicio or int(opcion) > fin:
		print("\nERROR: debe estar dentro del rango especificado.")
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
		cargaAutomatica(usuarios, bicicletas, estaciones)
	elif opcionElegida == 1 and opcionSubmenu == 2:
		cargaAutomaticaAleatoria()
	elif opcionElegida == 2 and opcionSubmenu == 1:
		listado()
	elif opcionElegida == 2 and opcionSubmenu == 2:
		alta(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 3:
		modificacion()
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

def cargaAutomatica(usuarios, bicicletas, estaciones):
	generarUsuarios(usuarios) # En el módulo generarEstructuras
	generarBicicletas(bicicletas) # En el módulo generarEstructuras
	generarEstaciones(estaciones) # En el módulo generarEstructuras
	print("\n\n[INFO] Se ha realizado una carga de datos de usuarios, bicicletas y estaciones predefinidas.\nVolviendo al submenú de carga de datos...")

"""
def alta(usuarios):
	dni = int(input("Ingrese su DNI: "))
	if dni in usuarios:
		print("El usuario ya está en el sistema. Volviendo al menu principal.")
	else:
		pin = input("Ingrese un PIN de 4 dígitos: ")
		nombre = input("Ingrese su nombre: ")
		apellido = input("Ingrese su apellido: ")
		celular = input("Ingrese su celular: ")
		usuarios[dni] = [pin, nombre.lower() + "_" + apellido.lower(), celular]
"""
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
		print('[ERROR] El DNI ingresado ya se asociado a una cuenta en el sistema. Volviendo al menú principal...')
		# aca deberia darle la opcion de volver manualmente porque sino apenas imprime 
		# sale al menu principal sin dejar leer el mensaje

def menuUsuario(usuarios):
	dni, pin = iniciarSesion(usuarios) 
	if dni != 0:
		opcionElegida = 0
		while opcionElegida != 4:
			imprimirMenuUsuario()
			opcionElegida = ingresarEntreRangos(1,4,"Ingrese el número de opción (1 a 4): ")
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
		print("No hay una cuenta registrada con ese DNI, volviendo al menu principal...")
		return 0, 0

def submenuUsuario(usuarios, opcionElegida, dni, pin):
	if opcionElegida == 1:
		cambiarPin(usuarios, dni, pin)
	elif opcionElegida == 2:
		retirarBicicleta()
	elif opcionElegida == 3:
		devolverBicicleta()
	print(usuarios)

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
	print("[MENSAJE] El PIN fue cambiado con éxito. Volviendo al menú del usuario...")


main()
