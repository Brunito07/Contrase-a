
#Programa que valide si una contraseña ingresada por el usuario es segura
#Una contraseña segura:
#-->Tiene mas de 8 caracteres,
#-->Tiene una letra mayuscula
#-->Tiene al menos un numero


def comprobarContrasenia(password):
	largo = False
	mayus = False
	numer = False
	if len(password) > 8:
		largo = True
	for i in range (len(password)):
		if password[i].isupper():
			mayus = True
		if password[i].isnumeric():
			numer = True
	if largo and mayus and numer:
		return True
	else:
		return False

password = input("Ingrese una contraseña: ")

verificacion = comprobarContrasenia(password)
if verificacion:
	print("La contraseña es segura")
else:
	print("La contraseña no es segura")

