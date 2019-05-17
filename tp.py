from imprimirMenus import *
from generarEstructuras import *
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
		menuUsuario()

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
		print(usuarios)
	elif opcionElegida == 1 and opcionSubmenu == 2:
		cargaAutomaticaAleatoria()
	elif opcionElegida == 2 and opcionSubmenu == 1:
		listado()
	elif opcionElegida == 2 and opcionSubmenu == 2:
		alta(usuarios)
		print(usuarios)
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

def alta(usuarios):

def menuUsuario():
	print("**** MENU USUARIO *****")
	print("FIN DEL PROGRAMA")

main()
