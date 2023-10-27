
import string
import random
def generar_minusculas(minusculas):
    caracter = string.ascii_lowercase
    cantidad_minusculas = ""
    for j in range(minusculas):
        cantidad_minusculas += random.choice(caracter)
        print(cantidad_minusculas)