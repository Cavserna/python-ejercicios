while True:
        try:
           longitud= int(input("Ingrese la longitud deseada: ")) 
           break
        except ValueError:
           print("Ingrese un numero entero válido")   
                        
                        
                        
                        
while True:
          try:
            mayusculas = int(input("Ingrese el número de mayúsculas que desea: "))
            break
          except ValueError:
             print("Ingrese un numero entero válido")
                                    
                        
while True:
          try:
             minusculas= int(input("Ingrese el número de minúsculas que desea: "))
             break
          except ValueError:
             print("Ingrese un numero entero válido")            
                                    
while True:
          try:
             numeros= int(input("Ingrese la cantidad de números que desea: "))
             break
          except ValueError:
             print("Ingrese un numero entero válido")  



caracteres_totales= mayusculas+minusculas+numeros

if longitud < caracteres_totales:
    





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



while longitud < caracteres_totales:
        try:
          
          while True:
                   try:
                      longitud= int(input("Ingrese la longitud deseada: ")) 
                      break
                   except ValueError:
                     print("Ingrese un numero entero válido")   

                    
          while True:
                   try:
                      mayusculas = int(input("Ingrese el número de mayúsculas que desea: "))
                      break
                   except ValueError:
                     print("Ingrese un numero entero válido")
                                
                    
          while True:
                   try:
                      minusculas= int(input("Ingrese el número de minúsculas que desea: "))
                      break
                   except ValueError:
                     print("Ingrese un numero entero válido")            
                                
          while True:
                   try:
                      numeros= int(input("Ingrese la cantidad de números que desea: "))
                      break
                   except ValueError:
                      print("Ingrese un numero entero válido")           
                   
        except ValueError:
           print("La longitud no puede ser menor a la cantidad de carácteres elegidos")
        
        