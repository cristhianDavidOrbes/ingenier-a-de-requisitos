
comprovante1 = 0
comprovante2 = 0
puntos = 0
import json

def informacion(nombre,edad, tarjeta,vencimiento,contraseña, puntos):
    usuario ={
          'nombre': nombre,
          'tarjeta': tarjeta,
          'vencimiento': vencimiento,
          'contraseña': contraseña,
          'edad': edad,
          'puntos': puntos
        }
    with open("datos.json",'w') as archivo:
       json.dump(usuario,archivo)
    with open("datos.json",'r') as archivo:
      base_de_datos = json.load(archivo)
      return base_de_datos
def escritura():
  with open("datos.json",'r') as archivo:
      base_de_datos = json.load(archivo)
      return base_de_datos
  
volver = 0

while(volver == 0):
  data1 = escritura()
  verificacion1 = data1['nombre']
  verificacion2 = data1['contraseña']
  print("bienvenido a la aplicacion \n"  "1. registrarse \n"  "2. inicio de sesion \n"  "3. salir " )
  Elección = int(input()) 
  match(Elección):
     case int(1):
       nombre = input("digite su nombre: ")
       edad = input("digite su edad: ")
       contraseña  = input("digite su contraseña: ")
       tarjeta = input("digite el número de la tarjeta de crédito: ")
       vencimiento = input("digite el vencimiento de su tarjeta de credito: ")
       data = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos = 0)
       print("ya esta registrado volviendo al menu de inicio")
       verificacion1 = data['nombre']
       verificacion2 = data['contraseña']
       

     case int(2):
       verificacion1 = data['nombre']
       verificacion2 = data['contraseña']
       while(comprovante1 != verificacion1 and comprovante2 != verificacion2):
         comprovante1 = input("porfavor digite su usuario: ")
         comprovante2 = input("porfavor digite su contraseña: ")
         data = informacion(nombre,edad, tarjeta,vencimiento,contraseña, puntos)
         print("incorrecto")
       print("ingreso correctamente")
       print("1. compra de aplicaciones \n", "2. canjeo de premios \n", "3.inicio" )
       entrada = int(input())
       match(entrada):
         case int(1):
           print("bienbenido a compras de aplicaciones \n", "1. snapshap hd \n", "valor: 10000 \n " "2.cara libro ", "valor:37000 \n")
           print("3. tutube \n", "valor: 30000 \n " "4.pajaro x \n ", "valor:50000 \n","5.gpt 7 \n", " valor: 100000")
           entrada1 = int(input())
           match(entrada1):
             case int(1):
               print("felisitaciones por tu compra resiviste 10 puntos de bonificacion")
               puntos = puntos + 10
               datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
             case int(2):
               print("felisitaciones por tu compra resiviste 20 puntos de bonificacion")
               puntos = puntos + 20
               datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
             case int(3):
               print("felisitaciones por tu compra resiviste 40 puntos de bonificacion")
               puntos = puntos + 40
               datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
             case int(4):
               print("felisitaciones por tu compra resiviste 5 puntos de bonificacion")
               puntos = puntos + 5
               datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
             case int(5):
               print("felicitaciones por tu compra resiviste 25 puntos de bonificacion")
               puntos = puntos + 25
               datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
         case int(2):
           print("bienvenido al canjeo de premios si tiene suficientes puntos \n","selecccione el que mas le guste" )
           datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
           total = datos4['puntos']
           print("usted tiene total de puntos: ",total)
           if(total > 12):
             print("1. pelota \n","valor 75 puntos \n","2. audifonos \n","valor 60 puntos \n","3. gorra \n","valor 12 puntos \n","4. drone \n","valor 50 puntos \n","5. celular \n","valor 100 puntos \n")
             regalo = int(input())
             match(regalo):
               case int(1):
                 puntos = total - 75
                 datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
                 total = datos4['puntos']
                 print("usted gano una pelota ahora tiene ",total, " de puntos")
               case int(2):
                 puntos = total - 60
                 datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
                 total = datos4['puntos']
                 print("usted gano una audifonos  ahora tiene ",total, " de puntos")
               case int(3):
                 puntos = total - 12
                 datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
                 total = datos4['puntos']
                 print("usted gano una gorra ahora tiene ",total, " de puntos")
               case int(4):
                 puntos = total - 50
                 datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
                 total = datos4['puntos']
                 print("usted gano una drone ahora tiene ",total, " de puntos")
               case int(5):
                 puntos = total - 100
                 datos4 = informacion(nombre,edad, tarjeta,vencimiento,contraseña,puntos)
                 total = datos4['puntos']
                 print("usted gano una celular ahora tiene ",total, " de puntos")
               case _:
                 print("profavor seleccione los refalos disponibles")
           else:
             print("usted no tiene los puntos suficientes para reclamar")

         case int(3):
           print("volviendo al inicio")
     case int(3):
            
       volver =1
          
         
       
  
    
