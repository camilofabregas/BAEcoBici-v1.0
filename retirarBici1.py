import random 
from validaciones import *

def retirarBicicleta (usuarios, bicicletas, estaciones, dni):
	idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Ingrese el numero de identificacion de la estacion donde desea retirar la bicicleta: "))
	while idEstacion not in estaciones:
		listadoEstaciones = input("[ERROR] Numero de identificacion invalido.\nDesea ver las estaciones disponibles? s/n: ")
		if listadoEstaciones == "s":
			print ("\n")
			for identificador in estaciones:
				print(estaciones[identificador]["Dirección"],": N°", identificador, ". Tiene {} bicicletas ancladas.".format(len(estaciones[identificador]["Bicicletas"])))
			print ("\n")
		idEstacion = int(solicitarValidarDigitos(1, len(estaciones), "[SOLICITUD] Por favor, ingrese un numero entre 1 y {}: ".format(len(estaciones))))
	if len(estaciones[idEstacion]["Bicicletas"]) == 0:
		print("[INFO] La estacion {} no dispone de ninguna bicicleta libre en ella. Intente con otra estacion.".format(estaciones[idEstacion]["Dirección"]))
	elif len(estaciones[idEstacion]["Bicicletas"]) > 0:
		bicicletaRetirada = random.choice(estaciones[idEstacion]["Bicicletas"])
		while bicicletas[bicicletaRetirada] == ["Necesita reparación", "En reparación"]:
			bicicletaRetirada = random.choice(estaciones[idEstacion]["Bicicletas"])
		estaciones[idEstacion]["Bicicletas"].remove(bicicletaRetirada)
		bicicletas[bicicletaRetirada] = ["En condiciones", "En circulacion"]
		print("[INFO] El usuario {} retiro la bicicleta N° {} en la estacion {} con exito. \n\n".format(dni,bicicletaRetirada, estaciones[idEstacion]["Dirección"]))

# HAY QUE CAMBIAR EN TP.PY
# AGREGAR AL PRINCIPIO FROM retirarBici1 IMPORT *
# LINEA 36 menuUsuario(usuarios, bicicletas,estaciones)
# LINEA 122 def menuUsuario(usuarios, bicicletas, estaciones):
# LINEA 129 submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin)
# LINEA 143 def submenuUsuario(usuarios, bicicletas, estaciones, opcionElegida, dni, pin):
# LINEA 147 retirarBicicleta(usuarios, bicicletas, estaciones, dni)
