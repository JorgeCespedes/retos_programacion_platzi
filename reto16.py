lista_numero = []

def suma_numeros():
  print('Suma de los números')
  print('Presiona 0 para terminar las operaciones')
  while True:
    numero = int(input('ingresa los numeros: '))
    lista_numero.append(numero)

    if numero == 0:
      print('Los numeros ingresados suman: ',sum(lista_numero))
      break

def multiplica_numeros():
  print('Multiplica de los números')
  print('Presiona 0 para terminar las operaciones')
  while True:
    numero = int(input('ingresa los numeros: '))
    lista_numero.append(numero)

    producto = 1
    for i in lista_numero[0:-1]:
      producto *= i

    if numero == 0:
      print('Los numeros ingresados multiplican: ', producto)
      break


def run():
  while True:
    operacion = str(input('''
        Qué operación desea realizar:
        [s] Suma
        [m] Multiplicación
        [x] Salir
        '''))

    if operacion == 's':
      suma_numeros()

    elif operacion == 'm':
      multiplica_numeros()

    elif operacion == 'x':
      break

    else:
      print('Operación desconocida.')

if __name__ == "__main__":
  run()