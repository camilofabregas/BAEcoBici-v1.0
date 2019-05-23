from imprimirMenus import *
from generarEstructuras import *
from validaciones import *
import random
import datetime
import os

def main():
	usuarios, bicicletas, estaciones, usuariosEnViaje = dict(), dict(), dict(), dict() # Defino los diccionarios vacíos.
	imprimirLogo() # En el módulo menuYSubmenus
	menuPrincipal(usuarios, bicicletas, estaciones, usuariosEnViaje)

def limpiarPantalla():
	if os.name == "nt":
		return os.system("cls")
	else:
		return os.system("clear")

def menuPrincipal(usuarios, bicicletas, estaciones, usuariosEnViaje):
	opcionElegida = 0
	while opcionElegida != 6:
		imprimirMenuPrincipal() # En el módulo menuYSubmenus
		opcionElegida = ingresarEntreRangos(1,6,"[SOLICITUD] Ingrese el número de opción (1 a 6): ")
		submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, usuariosEnViaje)
		limpiarPantalla()

def ingresarEntreRangos(inicio, fin, mensaje): #Para ingresar (y validar) una opción dentro de un rango especifico.
	opcion = input(mensaje)
	while not opcion.isdigit() or int(opcion) < inicio or int(opcion) > fin:
		print("\n[ERROR] Debe estar dentro del rango especificado.")
		opcion = input(mensaje)
	return int(opcion)

def submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, usuariosEnViaje): # Genera el submenu de la opción que elegí en el menu principal
	if opcionElegida != 5 and opcionElegida != 6: # Si no es "Salir del programa" o "Ingresar al sistema"
		rangoSubmenuElegido = calcularRangoSubmenuElegido(opcionElegida)
		opcionSubmenu = 0
		while opcionSubmenu != rangoSubmenuElegido:
			imprimirSubmenuElegido(opcionElegida) # En el módulo menuYSubmenus
			opcionSubmenu = ingresarEntreRangos(1,rangoSubmenuElegido,"[SOLICITUD] Ingrese el número de opción (1 a {}): ".format(rangoSubmenuElegido))
			invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones)
	elif opcionElegida == 5:
		menuUsuario(usuarios, bicicletas, estaciones, usuariosEnViaje)

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
		desbloquear(usuarios)
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

				
def imprimirUsuariosBloqueados (usuarios):
    cantidadUsuariosBloqueados = 0 #Indice para imprimir ordenado
    print("**** Usuarios Bloqueados ****")
    for usuario in usuarios:
        if usuarios[usuario][0] == "": #Filtro del diccionario los usarios bloqueados
            cantidadUsuariosBloqueados += 1
            print("{}. {} con dni {}".format(cantidadUsuariosBloqueados, usuarios[usuario][1], usuario)) #imprimo indice, nombre de usuario y dni
    return cantidadUsuariosBloqueados

def generarPin():
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    num3 = random.choice('0123456789')
    num4 = random.choice('0123456789')
    nuevoPin = num + num2 + num3 + num4 
    return nuevoPin

def desbloquear (usuarios):
    cantidadUsuariosBloqueados = imprimirUsuariosBloqueados(usuarios)
    if cantidadUsuariosBloqueados > 0:
        clave = input("Ingrese palabra secreta de desbloqueo: ")
        if clave == "shimano":
            usuarioElegido = int(input("Ingrese el DNI del usuario a desbloquear: "))
            while usuarioElegido not in usuarios or usuarios[usuarioElegido][0] != "":
                usuarioElegido = int(input("[ERROR] Debe ingresar el DNI de un usuario bloqueado: "))
            usuarios[usuarioElegido][0] = generarPin()
            print("[INFO] Usuario desbloqueado exitosamente. Se le generó el pin {}, a {}.".format(usuarios[usuarioElegido][0], usuarios[usuarioElegido][1]))
        else:
            print("[ERROR] Palabra incorrecta")
    else:
        print("No hay usuarios bloqueados")
    print("[INFO] Volviendo al submenu...")				
				
				
def menuUsuario(usuarios, bicicletas, estaciones, usuariosEnViaje):
	dni, pin = iniciarSesion(usuarios) 
	if dni != 0:
		opcionElegida = 0
		while opcionElegida != 4:
			imprimirMenuUsuario()
			opcionElegida = ingresarEntreRangos(1,4,"[SOLICITUD] Ingrese el número de opción (1 a 4): ")
			submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin, usuariosEnViaje)

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

def submenuUsuario(usuarios,bicicletas, estaciones, opcionElegida, dni, pin, usuariosEnViaje):
	if opcionElegida == 1:
		cambiarPin(usuarios, dni, pin)
	elif opcionElegida == 2:
		retirarBicicleta(usuarios, bicicletas, estaciones, dni, usuariosEnViaje)
	elif opcionElegida == 3:
		devolverBicicleta(estaciones, usuarios, dni, usuariosEnViaje)

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

def retirarBicicleta (usuarios, bicicletas, estaciones, dni, usuariosEnViaje):
	if dni in usuariosEnViaje:
		print("El usuario {} actualmente se encuentra en viaje, no puede retirar otra bicicleta.".format(dni))
	elif usuarios[dni][0] == "":
		print("[INFO] El usuario se encuentra actualmente bloqueado. Invalidando acción")
	else:
		contador = 3
		pin = input("[SOLICITUD] Ingrese su numero de PIN: ")
		while contador != 0 and pin != usuarios[dni][0]:
			contador -= 1
			pin = input("[ERROR] Por favor, ingrese su numero de pin correctamente. Tiene {} intentos restantes: ".format(contador))
			if contador == 0:
				usuarios[dni][0] = ""
				print ("[INFO] El usuario {} fue bloqueado porque excedio la cantidad de intentos permitida".format(dni))
				return None
		listadoEstaciones = input("[INFO] Desea ver las estaciones disponibles? s/n: ")
		if listadoEstaciones == "s":
			print ("\n")
			for identificador in estaciones:
				print(estaciones[identificador]["Dirección"],": N°", identificador, ". Tiene {} bicicletas ancladas.".format(len(estaciones[identificador]["Bicicletas"])))
			print ("\n")
		idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
		while idEstacion not in estaciones:
			idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Por favor, ingrese un numero entre 1 y {}: ".format(len(estaciones))))
		if len(estaciones[idEstacion]["Bicicletas"]) == 0:
			print("[INFO] La estacion {} no dispone de ninguna bicicleta libre en ella. Intente con otra estacion.".format(estaciones[idEstacion]["Dirección"]))
		elif len(estaciones[idEstacion]["Bicicletas"]) > 0:
			anclajeParaRetirar = random.randrange(1,len(estaciones[idEstacion]["Bicicletas"]))
			bicicletaRetirada = estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar]
			print("[SOLICITUD] Acerquese al anclaje {} y retire la bicicleta {}.\n".format(anclajeParaRetirar,bicicletaRetirada))
			estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar] = ""
			horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
			while (horas == 22) and (minutos > 44):
				horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
			horarioSalida = time(horas, minutos, segundos)
			bicicletas[bicicletaRetirada] = ["En condiciones", "En circulacion"]
			print("[INFO] El usuario {} retiro la bicicleta N° {} en la estacion {} del anclaje {} a las {} hs. con exito. \n\n".format(dni,bicicletaRetirada, estaciones[idEstacion]["Dirección"], anclajeParaRetirar, horarioSalida))
		usuariosEnViaje[dni] = [bicicletaRetirada, estaciones[idEstacion]["Dirección"], horarioSalida]
		
def devolverBicicleta(estaciones, usuarios, dni, bicicletas, usuariosEnViaje):
    print("**** ESTACIONES ****")
    for estacion in estaciones:
        print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
    idEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
    while idEstacion not in estaciones:
        idEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))
    if len(estaciones[idEstacion]["Bicicletas"]) >= estaciones[idEstacion]["Capacidad"]:
        print("[INFO] No hay lugar en esta estación para anclar su bicicleta. Por favor diríjase hacia otra estación.")
    else:
        idBicicleta = usuariosEnViaje[dni][1]
        estadoBici = input("[SOLICITUD] ¿Necesita reparación la bicicleta? s/n: ")
        if estadoBici == "s":
            bicicletas[idBicicleta][0] = "Necesita reparación"
            bicicletas[idBicicleta][1] = "En reparación"
            print("[INFO] La bicicleta se enviará a reparación.")
        print (bicicletas)
        generarDuracionDeViaje(usuarios, dni)
        del(usuariosEnViaje[dni])


def generarDuracionDeViaje(usuarios, dni):
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    duracionViaje = num + num2
    while int(duracionViaje) < 5 or int(duracionViaje) > 75:
    	num = random.choice('0123456789')
    	num2 = random.choice('0123456789')
    	duracionViaje = num + num2
    if int(duracionViaje) > 60:
    	print("[INFO] Su viaje exedió el límite de una hora. Su usuario ha sido bloqueado.")
    	usuarios[dni][0] = ""
    else:
    	print("Su viaje duró {} minutos.".format(int(duracionViaje)))
		
	
def horarios (horaMinimo, minutosMinimo, segundosMinimo, horaMaximo, minutosMaximo, segundosMaximo):
		horas = random.randrange(horaMinimo, horaMaximo)
		minutos = random.randrange(minutosMinimo, minutosMaximo)
		segundos = random.randrange(segundosMinimo, segundosMaximo)
		return (horas, minutos, segundos)


main()
