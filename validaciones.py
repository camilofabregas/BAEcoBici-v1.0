def solicitarValidarDigitos(mini, maxi, msj):
	dato = input(msj)
	while not dato.isdigit() or len(dato)< mini or len(dato)> maxi:
		if mini != maxi:
			print("\n[ERROR] El dato debe estar expresado en números y con una longitud de {} a {} caracteres.".format(mini, maxi))
		else:
			print("\n[ERROR] El dato debe estar expresado en números y con una longitud de {} caracteres.".format(maxi))
		dato = input(msj)
	return dato

def solicitarValidarDatos(msj):
	dato = input(msj)
	while not dato.isalpha():
		print("\n[ERROR] El dato debe estar expresado unicamente en caracteres, sin símbolos especiales y sin espacios.")
		dato = input(msj)
	return dato.lower() 

def solicitarValidarCelular():
	contCaracteres = 0
	while cont < 8:
		celular = input("[SOLICITUD] Ingrese su celular(caracteres permitidos: '( ) + -' y numeros): ")
		contNumeros = 0
		for caracter in celular:
			if caracter.isdigit():
				cont+=1
			elif caracter not in ["(", "+", "-", ")"]:
				celular = input("[SOLICITUD] Ingrese celular(caracteres permitidos: '( ) + -' y numeros): ")
	return celular
