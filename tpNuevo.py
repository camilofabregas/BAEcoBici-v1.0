from imprimirMenus import *
from generarEstructuras import *
from validaciones import *
from viajeAleatorio import *
import random
import datetime
import os

def main():
	usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados = dict(), dict(), dict(), dict(), dict() # Defino los diccionarios vacíos.
	imprimirLogo() # En el módulo menuYSubmenus
	menuPrincipal(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)

def limpiarPantalla():
	if os.name == "nt":
		return os.system("cls")
	else:
		return os.system("clear")

def menuPrincipal(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados):
	opcionElegida = 0
	while opcionElegida != 6:
		imprimirMenuPrincipal() # En el módulo menuYSubmenus
		opcionElegida = ingresarEntreRangos(1,6,"[SOLICITUD] Ingrese el número de opción (1 a 6): ")
		submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)

def ingresarEntreRangos(inicio, fin, mensaje): #Para ingresar (y validar) una opción dentro de un rango especifico.
	opcion = input(mensaje)
	while not opcion.isdigit() or int(opcion) < inicio or int(opcion) > fin:
		print("\n[ERROR] Debe estar dentro del rango especificado.")
		opcion = input(mensaje)
	limpiarPantalla()
	return int(opcion)

def submenuElegido(opcionElegida, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados): # Genera el submenu de la opción que elegí en el menu principal
	if opcionElegida != 5 and opcionElegida != 6: # Si no es ni "Salir del programa" ni "Ingresar al sistema"
		rangoSubmenuElegido = calcularRangoSubmenuElegido(opcionElegida)
		opcionSubmenu = 0
		while opcionSubmenu != rangoSubmenuElegido:
			imprimirSubmenuElegido(opcionElegida) # En el módulo menuYSubmenus
			opcionSubmenu = ingresarEntreRangos(1,rangoSubmenuElegido,"[SOLICITUD] Ingrese el número de opción (1 a {}): ".format(rangoSubmenuElegido))
			invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)
	elif opcionElegida == 5:
		menuUsuario(usuarios, bicicletas, estaciones, viajesEnCurso)
	else:
		exit()

def calcularRangoSubmenuElegido(opcionElegida):
	if opcionElegida == 1 or opcionElegida == 3:
		return 3
	elif opcionElegida == 2 or opcionElegida == 4:
		return 5

def invocarFuncionSubmenuElegido(opcionElegida, opcionSubmenu, usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados):
	if opcionElegida == 1 and opcionSubmenu == 1:
		cargarDatos(usuarios, bicicletas, estaciones, "predefinida")
	elif opcionElegida == 1 and opcionSubmenu == 2:
		cargarDatos(usuarios, bicicletas, estaciones, "aleatoria") # Idem pero cambia la distribución de bicicletas.
	elif opcionElegida == 2 and opcionSubmenu == 1:
		listado(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 2:
		alta(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 3:
		modificacion(usuarios)
	elif opcionElegida == 2 and opcionSubmenu == 4:
		desbloquear(usuarios)
	elif opcionElegida == 3 and opcionSubmenu == 1:
		viajeAleatorio(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)
	elif opcionElegida == 3 and opcionSubmenu == 2:
		viajesAleatoriosMultiples(usuarios, bicicletas, estaciones, viajesEnCurso, viajesFinalizados)
	elif opcionElegida == 4 and opcionSubmenu == 1:
		topUsuariosCantidadViajes(usuarios, viajesFinalizados)
	elif opcionElegida == 4 and opcionSubmenu == 2:
		topUsuariosDuracionViajes()
	elif opcionElegida == 4 and opcionSubmenu == 3:
		bicicletasEnReparacion(bicicletas)
	elif opcionElegida == 4 and opcionSubmenu == 4:
		estacionesMasActivas(estaciones, viajesFinalizados)

def cargarDatos(usuarios, bicicletas, estaciones, tipoDeCarga):
	generarUsuarios(usuarios) # En el módulo generarEstructuras
	generarBicicletas(bicicletas) # En el módulo generarEstructuras
	generarEstaciones(estaciones, bicicletas, tipoDeCarga) # En el módulo generarEstructuras
	limpiarPantalla()
	print("\n\n[INFO] Se ha realizado una carga automática {} de datos de usuarios, bicicletas y estaciones.\n[INFO] Volviendo al submenú de carga de datos...".format(tipoDeCarga))

def listado(usuarios):
    lista = []
    cont = 0
    for dni, datos in zip(list(usuarios.keys()), list(usuarios.values())):
        lista.append((dni, datos))
    lista.sort(key=lambda x:x[1][1])
    print("\n\n**** LISTADO DE USUARIOS ****")
    for usuario in lista:
        cont +=1
        print("{}. {}, DNI {}, PIN {}, Celular {}".format(cont, usuario[1][1], usuario[0], usuario[1][0], usuario[1][2]))

def alta(usuarios):
	dni = int(solicitarValidarDigitos(7, 8, "\n[SOLICITUD] Ingrese su DNI (sin puntos ni espacios): "))
	if dni not in usuarios:
		pin = solicitarValidarDigitos(4, 4, "[SOLICITUD] Ingrese un PIN de 4 dígitos: ")
		nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
		apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
		celular = solicitarValidarCelular()
		usuarios[dni] = [pin, nombre + "_" + apellido, celular]
		limpiarPantalla() 
		print("\n[EXITO] ¡Felicitaciones, {}, te has registrado con éxito!".format(nombre + "_" + apellido))
		return usuarios
	else:
		print("\n\n[ERROR] El DNI ingresado ya está asociado a una cuenta en el sistema. Volviendo al menú principal...")

def modificacion (usuarios):
	opcionElegida = 0 
	while opcionElegida != 5:
		imprimirMenuModificacion()
		opcionElegida = ingresarEntreRangos(1, 5, "[SOLICITUD] Ingrese el número de opción (1 a 5): ")
		if opcionElegida != 5:
			dni = input("\n[SOLICITUD] Ingrese el DNI: ")
			if dni.isdigit() and int(dni) in usuarios:
				dni = int(dni)
				modificarPin(opcionElegida, usuarios, dni)
				modificarNomApe(opcionElegida, usuarios, dni)
				modificarCelular(opcionElegida, usuarios, dni)
				eliminarUsuario(opcionElegida, usuarios, dni)
			else:
				limpiarPantalla()
				print ("\n[ERROR] El DNI ingresado no se encuentra en el sistema. Volviendo al menu de modificación... \n")	

def modificarPin(opcionElegida, usuarios, dni):
	if opcionElegida == 1:
		pin = input("[SOLICITUD] Ingrese el PIN asociado: ")
		while usuarios[dni][0] != pin:
			print("\n[ERROR] El PIN ingresado no es correcto")
			pin = input("[SOLICITUD] Ingrese el PIN asociado: ")
		limpiarPantalla()
		cambiarPin(usuarios, dni, pin)
def modificarNomApe(opcionElegida, usuarios, dni):
	if opcionElegida == 2:
		nombre = solicitarValidarDatos("[SOLICITUD] Ingrese su nombre: ")
		apellido = solicitarValidarDatos("[SOLICITUD] Ingrese su apellido: ")
		usuarios[dni][1] = nombre + "_" + apellido
		print ("[INFO] Nombre y apellido del usuario {} fue cambiado con éxito.".format(dni))
def modificarCelular(opcionElegida, usuarios, dni):
	if opcionElegida == 3:
		celular = solicitarValidarCelular()
		usuarios [dni][2] = celular
		print ("[INFO] Celular del usuario {} cambiado con exito.".format(dni))
def eliminarUsuario(opcionElegida, usuarios, dni):
	if opcionElegida == 4:
		confirmacion = input("El usuario de DNI {} será eliminado. ¿Desea confirmar? s/n: ".format(dni))
		if confirmacion == "s":
			del usuarios[dni]
			print("[INFO] El usuario {} fue eliminado con éxito.".format(dni))
		else:
			print ("[INFO] Operacion cancelada. Volviendo al menu de modificación...\n")

def imprimirUsuariosBloqueados (usuarios):
    cantidadUsuariosBloqueados = 0 #Indice para imprimir ordenado
    print("**** USUARIOS BLOQUEADOS ****")
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
            usuarioElegido = int(solicitarValidarDigitos(7, 8, "Ingrese el DNI del usuario a desbloquear: "))
            while usuarioElegido not in usuarios or usuarios[usuarioElegido][0] != "":
                usuarioElegido = int(solicitarValidarDigitos(7, 8, "[ERROR] Debe ingresar el DNI de un usuario bloqueado: "))
            usuarios[usuarioElegido][0] = generarPin()
            print("[INFO] Usuario desbloqueado exitosamente. Se le generó el pin {}, a {}.".format(usuarios[usuarioElegido][0], usuarios[usuarioElegido][1]))
        else:
            print("[ERROR] Palabra incorrecta")
    else:
        print("No hay usuarios bloqueados")
    print("[INFO] Volviendo al submenu...")				
				
def menuUsuario(usuarios, bicicletas, estaciones, viajesEnCurso):
	dni, pin = iniciarSesion(usuarios)
	if dni != 0:
		opcionElegida = 0
		while opcionElegida != 4:
			imprimirMenuUsuario()
			opcionElegida = ingresarEntreRangos(1,4,"[SOLICITUD] Ingrese el número de opción (1 a 4): ")
			submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin, viajesEnCurso)

def iniciarSesion(usuarios):
	print("\n\n**** INICIAR SESIÓN ****")
	dni = input("[SOLICITUD] Ingrese su DNI: ")
	if dni.isdigit() and int(dni) in usuarios:
		if usuarios[int(dni)][0] == "":
			limpiarPantalla()
			print("\n[ERROR] Su cuenta se encuentra bloqueada, volviendo al menu principal...")
			return 0, 0
		pin = input("[SOLICITUD] Ingrese su PIN asociado: ")
		while pin != usuarios[int(dni)][0]:
			pin = input("\n[ERROR] PIN incorrecto, pruebe de nuevo.\n[SOLICITUD] Ingrese su PIN asociado: ")
		limpiarPantalla()
		print("\n[MENSAJE] Iniciaste sesión con éxito. ¡Bienvenido, {}!".format(usuarios[int(dni)][1]))
		return int(dni), pin
	else:
		limpiarPantalla()
		print("\n[ERROR] No hay una cuenta registrada con ese DNI, volviendo al menu principal...")
		return 0, 0

def submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin, viajesEnCurso):
	if opcionElegida == 1:
		cambiarPin(usuarios, dni, pin)
	elif opcionElegida == 2:
		retirarBicicleta(usuarios, bicicletas, estaciones, dni, viajesEnCurso)
	elif opcionElegida == 3:
		devolverBicicleta(estaciones, dni, viajesEnCurso, usuarios, bicicletas)

def cambiarPin(usuarios, dni, pinViejo):
	print("\n")
	pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
	while pinNuevo == pinViejo:
		print("\n[ERROR] El PIN ingresado ya está asociado a su cuenta.")
		pinNuevo = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese un nuevo PIN de 4 dígitos: ")
	pinNuevoRepetido = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
	while pinNuevo != pinNuevoRepetido:
		print("\n[ERROR] Los pines no coinciden, intente de nuevo...")
		pinNuevoRepetido = solicitarValidarDigitos(4, 4,"[SOLICITUD] Ingrese nuevamente el PIN deseado: ")
	usuarios[dni][0] = pinNuevo
	limpiarPantalla()
	print("\n[INFO] El PIN fue cambiado con éxito.")

def retirarBicicleta (usuarios, bicicletas, estaciones, dni, viajesEnCurso):# Verifica que el usuario no esté en viaje ni bloqueado y pide el PIN.
	if dni in viajesEnCurso or usuarios[dni][0] == "":
		print("[ERROR] El usuario {} está bloqueado o actualmente se encuentra en viaje.".format(usuarios[dni][0]))
	else:
		contador = 4
		pin = input("\n[SOLICITUD] Ingrese su numero de PIN: ")
		while contador > 1 and pin != usuarios[dni][0]:
			contador += -1
			pin = input("[ERROR] Por favor, ingrese su numero de pin correctamente. Tiene {} intentos restantes: ".format(contador))
			if contador == 1:
				usuarios[dni][0] = ""
				limpiarPantalla()
				print ("\n[INFO] El usuario {} fue bloqueado porque excedió la cantidad de intentos permitidos.".format(usuarios[dni][1]))
		elegirEstacionParaRetirar(estaciones, bicicletas, viajesEnCurso, dni)

def elegirEstacionParaRetirar(estaciones, bicicletas, viajesEnCurso, dni):
	print("\n**** ESTACIONES ****")
	for estacion in estaciones:
		print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
	idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "\n[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
	while idEstacion not in estaciones or len(estaciones[idEstacion]["Bicicletas"]) == 0:
		print("\n[ERROR] El número de estación ingresado es inválido o la estación se encuentra sin bicicletas.")
		idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
	asignarBicicleta(estaciones, bicicletas, viajesEnCurso, idEstacion, dni)

def asignarBicicleta(estaciones, bicicletas, viajesEnCurso, idEstacion, dni):
	anclajeParaRetirar = random.randrange(1,len(estaciones[idEstacion]["Bicicletas"]))
	while estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar] == "":
		anclajeParaRetirar = random.randrange(1,len(estaciones[idEstacion]["Bicicletas"]))
	bicicletaRetirada = estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar]
	limpiarPantalla()
	print("\n[EXITO] Acerquese al anclaje {} y retire la bicicleta {}.\n".format(anclajeParaRetirar,bicicletaRetirada))
	estaciones[idEstacion]["Bicicletas"][anclajeParaRetirar] = ""
	horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
	while (horas == 22) and (minutos > 44):
		horas, minutos, segundos = horarios (0, 0, 0, 23, 60, 60)
	horarioSalida = time(horas, minutos, segundos)
	bicicletas[bicicletaRetirada] = ["En condiciones", "En circulacion"]
	viajesEnCurso[dni] = [bicicletaRetirada, estaciones[idEstacion]["Dirección"], horarioSalida]
		
def devolverBicicleta(estaciones, dni, viajesEnCurso, usuarios, bicicletas):
    if dni not in viajesEnCurso:
        print("\n[INFO] Usted no ha retirado una bicicleta. Volviendo al submenu...")
    else:
        print("\n**** ESTACIONES ****")
        for estacion in estaciones:
            print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
        idEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
        while idEstacion not in estaciones:
            idEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))
        verificarLugar(idEstacion, estaciones, viajesEnCurso, usuarios, dni, bicicletas)

def verificarLugar(idEstacion, estaciones, viajesEnCurso, usuarios, dni, bicicletas): #Se fija si hay lugar en la estación elegida para anclar la bici.
	anclajesLibres = 0
	for anclaje in estaciones[idEstacion]["Bicicletas"]:
		if estaciones[idEstacion]["Bicicletas"][anclaje] == "":
			anclajesLibres += 1
	if len(estaciones[idEstacion]["Bicicletas"]) - anclajesLibres >= estaciones[idEstacion]["Capacidad"]:
		print("[INFO] No hay lugar en esta estación para anclar su bicicleta. Por favor diríjase hacia otra estación.")
	else:
		guardarBicicleta(idEstacion, viajesEnCurso, usuarios, dni, estaciones, bicicletas)

def guardarBicicleta(idEstacion, viajesEnCurso, usuarios, dni, estaciones, bicicletas): #Ancla bicicleta a estación elegida o la envía a reparar.
	idBicicleta = viajesEnCurso[dni][0]
	estadoBici = input("\n[SOLICITUD] ¿Necesita reparación la bicicleta? s/n: ")
	if estadoBici == "s":
		bicicletas[idBicicleta][0] = "Necesita reparación"
		bicicletas[idBicicleta][1] = "En reparación"
		generarDuracionDeViaje(usuarios, dni)
		print("[INFO] La bicicleta se enviará a reparación.")
	else:
		for anclaje in estaciones[idEstacion]["Bicicletas"]:
			if estaciones[idEstacion]["Bicicletas"][anclaje] == "":
				estaciones[idEstacion]["Bicicletas"][anclaje] = idBicicleta
				break #Fue la única manera que se nos ocurrió para que la función haga lo que queríamos
		bicicletas[idBicicleta][1] = "Anclada en estación"
		del(viajesEnCurso[dni])
		generarDuracionDeViaje(usuarios, dni)

def generarDuracionDeViaje(usuarios, dni):
    duracionViaje = random.randrange(5,76)
    if duracionViaje > 60:
    	limpiarPantalla()
    	print("\n[INFO] Su viaje exedió el límite de una hora. Su usuario ha sido bloqueado.")
    	usuarios[dni][0] = ""
    else:
    	limpiarPantalla()
    	print("\n[INFO] Su viaje duró {} minutos.".format(duracionViaje))
	
def horarios (horaMinimo, minutosMinimo, segundosMinimo, horaMaximo, minutosMaximo, segundosMaximo):
		horas = random.randrange(horaMinimo, horaMaximo)
		minutos = random.randrange(minutosMinimo, minutosMaximo)
		segundos = random.randrange(segundosMinimo, segundosMaximo)
		return (horas, minutos, segundos)

def topUsuariosCantidadViajes(usuarios, viajesFinalizados):
	top = {}
	for dni in viajesFinalizados:
		if len(top) <= 10:
			top[usuarios[dni][1]] = len(viajesFinalizados[dni])
	print("**** TOP 10 USUARIOS CON MAYOR CANTIDAD DE VIAJES ****")
	topOrdenado = sorted(top.items(), key = lambda x:x[1], reverse = True)
	for usuarios in topOrdenado:
		print("El usuario {} con {} viajes.".format(usuarios[0], usuarios[1]))

def bicicletasEnReparacion (bicicletas):
	bicisEnReparacion = []
	for bicicleta in bicicletas:
		if bicicletas[bicicleta][0] == "Necesita reparación":
			bicisEnReparacion.append(bicicleta)
	random.shuffle(bicisEnReparacion)
	print("\n**** DEPÓSITO DE BICICLETAS ****")
	for bicicleta in bicisEnReparacion:
		print("[INFO] La bicicleta {} necesita reparacion.".format(bicicleta))

def estacionesMasActivas(estaciones, viajesFinalizados):
	top = {}
	for dni in viajesFinalizados:
		for viajes in viajesFinalizados[dni]:
			if estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"] not in top:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"]] = 1
			else:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][1]]["Dirección"]] += 1
			if estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"] not in top:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"]] = 1
			else:
				top[estaciones[viajesFinalizados[dni][viajesFinalizados[dni].index(viajes)][3]]["Dirección"]] += 1
	print("\n**** ESTACIONES MÁS ACTIVAS ****")
	topOrdenado = sorted(top.items(), key = lambda x:x[1], reverse = True)
	for estaciones in topOrdenado:
		print("Estacion {} con {} retiros y devoluciones.".format(estaciones[0], estaciones[1]))

def viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
    usuariosDisponibles = [usuario for usuario in usuarios if usuarios[usuario][0] != "" and usuario not in usuariosEnViaje]
    if usuariosDisponibles:
        usuario = random.choice(usuariosDisponibles)
        estacionRetirar = random.randrange(1, 11)
        while len(estaciones[estacionRetirar]["Bicicletas"]) == 0:
            estacionRetirar = random.randrange(1, 11)
        anclajesDisponibles = list(estaciones[estacionRetirar]["Bicicletas"].keys())
        anclajeAsignado = random.choice(anclajesDisponibles)
        bicicletaAsignada = estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
        while bicicletas[bicicletaAsignada] == ["Necesita reparación", "En reparación"]:
            anclajeAsignado = random.choice(anclajesDisponibles)
            bicicletaAsignada = estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
        del estaciones[estacionRetirar]["Bicicletas"][anclajeAsignado]
        horaSalida, minSalida, segSalida = horarios(0, 0, 0, 23, 60, 60)
        while horaSalida == 22 and minSalida > 29:
            horaSalida, minSalida, segSalida = horarios(0, 0, 0, 23, 60, 60)
        print("\n{} retiró la bicicleta {} de la estación N°{} de {} a las {}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionRetirar, estaciones[estacionRetirar]["Dirección"], time(horaSalida, minSalida, segSalida)))
        estacionDevolver = random.randrange(1, 11)
        while estacionDevolver == estacionRetirar or len(estaciones[estacionDevolver]["Bicicletas"]) == estaciones[estacionDevolver]["Capacidad"]:
            estacionDevolver = random.randrange(1, 11)
        horaViaje, minViaje, segViaje = horarios(0, 0, 0, 2, 30, 60)  # maximo 90 minutos que equivale a 1:30:00hs
        horaLlegada, minLlegada, segLlegada = calcularHoraLlegada(horaSalida, minSalida, segSalida, horaViaje, minViaje, segViaje)
        print("{} devolvió la bicicleta {} en la estación N°{} de {} a las {}hs".format(usuarios[usuario][1], bicicletaAsignada, estacionDevolver, estaciones[estacionDevolver]["Dirección"], time(horaLlegada, minLlegada, segLlegada)))
        if horaViaje == 1 and minViaje >= 0:
            usuarios[usuario][0] = ""
            print("Al exceder los 60 minutos de uso ha sido bloqueado")
        if usuario not in viajesFinalizados:
            viajesFinalizados[usuario] = [(bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida), estacionDevolver, time(horaLlegada, minLlegada, segLlegada))]
        elif usuario in viajesFinalizados:  # acumula los viajes de un mismo usuario
            viajesFinalizados[usuario].append((bicicletaAsignada, estacionRetirar, time(horaSalida, minSalida, segSalida) , estacionDevolver, time(horaLlegada, minLlegada, segLlegada)))  # no me funciona el time()
    else:
        return "None"

def calcularHoraLlegada(horas, minutos, segundos, horaViaje, minViaje, segViaje):
    horaLlegada = horas + horaViaje
    minLlegada = minutos + minViaje
    segLlegada = segundos + segViaje
    if segLlegada >= 60:
        segLlegada = segLlegada - 60
        minLlegada += 1
    if minLlegada >= 60:
        minLlegada = minLlegada - 60
        horaLlegada +=1
    return (horaLlegada, minLlegada, segLlegada)

def viajesAleatoriosMultiples(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados):
    cantidad = ingresarEntreRangos(1, 100, "Ingrese entre 1 y 100 la cantidad de viajes aleatorios que desea generar: ")
    for viaje in range(cantidad):
        viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados)
        if viajeAleatorio(usuarios, bicicletas, estaciones, usuariosEnViaje, viajesFinalizados) == "None":
            return print("[INFO] No hay mas usuarios disponibles. Se encuentran todos en viaje o bloqueados.")

main()
