import validaciones
import random
import generarEstructuras

def devolverBici(usuarios, estaciones):
	dniUsuario = int(solicitarValidarDigitos(7, 8, "[SOLICITUD] Ingrese su DNI: "))
	if dniUsuario not in usuarios:
		dniUsuario = int(solicitarValidarDigitos(7, 8, "[ERROR] Ingrese un DNI registrado al sistema: "))
	numEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
	if numEstacion not in estaciones:
		numEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))
	return dniUsuario

def generarDuracionDeViaje():
	num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    duracionViaje = num + num2
    if int(duracionViaje) < 5:
    	generarEstructuras()
    return duracionViaje

def validarDuracion(duracionViaje, usuarios, dniUsuario):
	if int(duracionViaje) > 75:
		print("[INFO] Su viaje exedió el límite de los 75 minutos. Su usuario ha sido bloqueado.")
		usuarios[dniUsuario][0] == " "
	else:
		print("Su viaje duró {} minutos.".format(int(duracionViaje)))