from validaciones import*
import random

def devolverBicicleta(estaciones, usuarios):
	print("**** ESTACIONES ****")
	for estacion in estaciones:
		print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
	idEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
	while idEstacion not in estaciones:
		idEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))
	if estaciones[idEstacion]["Bicicletas"] == 0:
		print("[INFO] No hay más lugar en esta estación. Por favor, devuelvala en otra.")
	else:
		print("[INFO] Se devolvió la bici con éxito.")
		estaciones[idEstacion]["Bicicletas"] += 1

	generarDuracionDeViaje(usuarios)


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
