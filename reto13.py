lista_precio = []

def calcular_recibo():
  precio_total = sum(lista_precio)
  propina = round(precio_total * .10,2)
  precio_final = precio_total + propina

  print('=== B O L E TA ===')
  print('Total de platillos pedidos: ', len(lista_precio))
  print('Precio total de los platillos: S/.', precio_total)
  print('Propina S/: ', propina)
  print('Precio Final S/ : ', precio_final)
  print('')
  print('Gracias por su visita')
  print('')

def run():

  precio_basico = 10
  precio_especial = 18
  precio_ejecutivo = 25
  while True:
    print(" === Restaurante === ")
    opcion = int(input('''
         Escoge tus platillo:
         [1] basico     S/ 10.0
         [2] especial   S/ 18.0
         [3] ejecutivo  S/ 25.0
         [4] calcular recibo
         [5] salir
          '''))
    if opcion == 1:
      print("Opcion 1, S/")
      lista_precio.append(precio_basico)
    elif opcion == 2:
      print("Opcion 2")
      lista_precio.append(precio_especial)
    elif opcion == 3:
      print("Opcion 3")
      lista_precio.append(precio_ejecutivo)
    elif opcion == 4:
      calcular_recibo()
      
    elif opcion == 5:
      break
    else:
      print("Opcion no valida")

if __name__ == '__main__':
  run()
