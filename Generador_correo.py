def datos(name, last_name, date):
    nom = name[:2]
    last = last_name[-2:]
    da = date[:2]
    correo = nom+last+da+"@gmail.com"
    print(correo)

name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
date = input("Ingresa tu fecha de nacimiento: ")
datos(name,last_name,date)