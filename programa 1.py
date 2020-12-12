if __name__ == '__main__':
	nombre = str()
	puerta = str()
	i = int()
	print("Ali Baba te pregunta ¿Cual es tu nombre?")
	nombre = input()
	print(" ¡Cual es la clave secreta?"," ",nombre, end="")
	print("")
	puerta = input()
	i = 1
	while True:
		if puerta=="abrete sesamo":
			print("Puerta Abierta","  ", end="")
		else:
			print("Clave Incorrecta. Haber ¿Cual es la clave? ",nombre,i,": ", end="")
			puerta = input()
			if puerta!="abrete sesamo":
				i = i+1
		if puerta=="abrete sesamo" or i==11: break
	if puerta=="abrete sesamo":
		print("Puerta Abierta")
	else:
		if i==11:
			print("Intentos fallidos, Puerta Cerrada")
