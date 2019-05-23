def listado(usuarios):
    lista = []
    cont = 0
    for dni, datos in zip(list(usuarios.keys()), list(usuarios.values())):
        lista.append((dni, datos))
    lista.sort(key=lambda x:x[1][1])
    print("\n\n**** Listado de Usuarios ****")
    for usuario in lista:
        cont +=1
        print("{}. {}, DNI {}, PIN {}, Celular {}".format(cont, usuario[1][1], usuario[0], usuario[1][0], usuario[1][2]))
        