import string
import random

mayusculas = int(input("Ingrese el número de mayúsculas: "))
minusculas= int(input("Ingrese el número de minúsculas: "))
numeros= int(input("Ingrese la cantidad de números: "))
longitud= int(input("Ingrese la longitud deseada: "))


def generar_caracteres (mayusculas):
    caracter = string.ascii_uppercase
    cantidad_mayusculas = ""
    for i in range(mayusculas):
        cantidad_mayusculas += random.choice(caracter)
        print(cantidad_mayusculas)
    
        
def generar_minusculas(minusculas):
    caracter = string.ascii_lowercase
    cantidad_minusculas = ""
    for j in range(minusculas):
        cantidad_minusculas += random.choice(caracter)
        print(cantidad_minusculas)

def generar_numeros(numeros):
    caracter= string.digits
    cantidad_numeros= ""
    for k in range(numeros):
        cantidad_numeros += random.choice(caracter)
        print ( cantidad_numeros )
        
generar_numeros(numeros)




