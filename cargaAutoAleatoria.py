    
import random
from generarEstructuras import *

def cargaAutomaticaAleatoria(usuarios, bicicletas, estaciones):
    generarUsuarios(usuarios)
    generarBicicletas(bicicletas)
    generarEstacionesRandom(estaciones, bicicletas)

def generarEstacionesRandom(estaciones, bicicletas):
    identificador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    direcciones = ["Parque Lezama", "Plaza de Mayo", "Retiro", "Facultad de Derecho", "Obelisco", "Congreso", "Constitución", "Parque Patricios", "Planetario", "Parque Centenario", "Alto Palermo"]
    latitudLongitud = [(-34.6261, -58.3684), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.5828, -58.3920), (-34.6037, -58.3814), (-34.6095, -58.3889), (-34.6266, -58.3811), (-34.6385, -58.4060), (-34.5717, -58.4112), (-34.6073, -58.4335), (-34.5890, -58.4100)]
    capacidad = [30, 25, 20, 30, 30, 25, 30, 15, 25, 30, 25]
    for dato1, dato2, dato3, dato4 in zip(identificador, direcciones, latitudLongitud, capacidad):
        estaciones[dato1] = {"Dirección": dato2, "Latitud y longitud": dato3, "Capacidad": dato4,}

    '''bicis = list(bicicletas.keys())
    for idEstacion in estaciones:
        estaciones[idEstacion]["Anclajes"] = []
        numAnclajes = random.randrange(0, estaciones[idEstacion]["Capacidad"])
        for anclaje in range(numAnclajes):                    
            biciAsignada = random.randrange(0, len(bicis))
            estaciones[idEstacion]["Anclajes"].append(bicis[biciAsignada])
            del(bicis[biciAsignada])
            print('cantidad = {}'.format(len(bicis)))
    print(estaciones)'''


    bicis = list(bicicletas.keys())
    for idEstacion in estaciones:
        estaciones[idEstacion]["Anclajes"] = []
        numAnclajes = random.randrange(0, estaciones[idEstacion]["Capacidad"])
        for anclaje in range(numAnclajes):
            while not len(bicis) == 0:                    
                biciAsignada = random.randrange(0, len(bicis))
                estaciones[idEstacion]["Anclajes"].append(bicis[biciAsignada])
                del(bicis[biciAsignada])
                print('cantidad = {}'.format(len(bicis)))
    print(estaciones)
