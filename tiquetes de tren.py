repetir = 1
while(repetir == 1):
  print("saludo cordial bienvenido al menu de inicio\n porfavor seleccione su destino deseado")
  print(" 1. campus nueva granada \n 2. centro comercial gran estacion \n 3. estacion simon bolivar \n 4. estacion la caro \n 5. estacion umng")
  destino = int(0)
  error = int(0)
  comprobante = int(0)
  precio = int(120003)
  while(destino == error ):
    destino = int(input("seleccione del uno al cinco: "))
    match destino:
        case int(1):
          print("el valor seria 12000 pesos") and error +1 
          precio = precio*1
        case int(2):
          print("el valor seria 24000 pesos") and error +1 
          precio = precio*2
        case int(3):
          print("el valor seria 36000 pesos") and error +1 
          precio = precio*3
        case int(4):
          print("el valor seria 48000 pesos") and error +1
          precio = precio*4 
        case int(5): 
         print("el valor seria 60000 pesos") and error +1 
         precio = precio*5
        case _:
          print("porfavor seleccione los destinos disponibles")
          destino = 0
  credito = int(input("porfavor ingresa el numero de su tarjeta de credito: "))
  comprobante = int(input("porfavor ingresa el numero de su cedula "))
  if(comprobante == 1081982):
     print("verificado, se expide el precio de",precio, "a su tarjeta de credito con numero ",comprobante)
  else:
     print("su cedula es invalida")
  print("quieres regresar al inicio o salir \n 1. inicio \n 2.salir: ")
  repetir = int(input())