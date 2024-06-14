import random

clave = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud= int(input("ingresa la longitud de tu contraseña: "))

Elemento= ""
for i in range(longitud):
    Elemento+= random.choice(clave)

print(Elemento)
