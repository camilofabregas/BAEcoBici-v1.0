from validaciones import*
import random

def devolverBicicleta(usuarios, estaciones):
	print("**** ESTACIONES ****")
	for estacion in estaciones:
		print("Estación {}: {}".format(estacion, estaciones[estacion]["Dirección"]))
	idEstacion = int(solicitarValidarDigitos(1, 10, "[SOLICITUD] Ingrese el número de la estación donde devolverá la bicicleta: "))
	while idEstacion not in estaciones:
		idEstacion = int(solicitarValidarDigitos(1, 10, "[ERROR]Ingrese un número de estación válido: "))


def generarDuracionDeViaje(usuarios):
    num = random.choice('0123456789')
    num2 = random.choice('0123456789')
    duracionViaje = num + num2
    if int(duracionViaje)<5:
        generarDuracionDeviaje(usuarios)
    elif int(duracionViaje)>60:
        print("[INFO] Su viaje exedió el límite de una hora. Su usuario ha sido bloqueado.")
    else:
        print("Su viaje duró {} minutos.".format(int(duracionViaje)))
