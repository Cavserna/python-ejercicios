import string
import random

#/ Se valida que las cantidades ingresadas sean válidas
print ("            BIENVENIDO AL GENERADOR DE CONTRASEÑAS")
print ("                    *******************")
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


#/ Se suman la cantidad de carácteres y números solicitados por el usuario

caracteres_totales= mayusculas+minusculas+numeros

#/ Se valida que la longitud sea mayor que la suma de carácteres y números

while longitud < caracteres_totales:
   try:
      print ("")
      print(f"ALERTA! Debe ingresar una longitud mayor a {caracteres_totales}")
      longitud= int(input ("Ingresa la nueva longitud: "))
      break
   except ValueError:
      print("Ingrese un numero entero válido")
           
         
#/ Función que se encarga de seleccionar de manera random los carácteres y números       

def generar_contrasena (mayusculas,minusculas,numeros,longitud):
   

   caracter1 = string.ascii_uppercase
   cantidad_mayusculas = ""
   for i in range(mayusculas):
      cantidad_mayusculas += random.choice(caracter1)
        
        
   caracter2 = string.ascii_lowercase
   cantidad_minusculas = ""
   for j in range(minusculas):
      cantidad_minusculas += random.choice(caracter2)
        
        
   caracter3= string.digits
   cantidad_numeros= ""
   for k in range(numeros):
      cantidad_numeros += random.choice(caracter3)
      
   #/ La longitud debe completarse con signos
   
   longitud_parcial = longitud -(mayusculas+minusculas+numeros)
   
   caracter4= string.punctuation
   signos= ""
   for n in range(longitud_parcial):
      signos += random.choice(caracter4)
   
   
   #/ Se suman todos los elementos elegidos de manera random
   total= (cantidad_mayusculas+cantidad_minusculas+cantidad_numeros+signos)
   
   
   #/ Se convierte a lista para desordenar los elementos
   convertir_a_lista= list(total)
   
   #/ Se desordenan los elementos 
   random.shuffle(convertir_a_lista)
   
   #/ Se unen a una cadena de strings
   contrasena= "" .join(convertir_a_lista)
   print("            ************** ")
   #/ Se imprime el resultado
   
   print (f" SU CONTRASEÑA ES: { contrasena}")
   print ("")
   print ("               ADIÓS")
   
generar_contrasena(mayusculas,minusculas,numeros,longitud)      
   
      





