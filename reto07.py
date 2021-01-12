import random

def game():
  listPlayerPC = ['piedra', 'papel', 'tijera']
  ptoPlayer1 = 0
  ptoPlayerPC = 0
  while True:
    aleatorio = random.randint(0,len(listPlayerPC))
    playerPC = listPlayerPC[aleatorio-1]

    player1 = str(input('''
        Escoge una opción:
          [s] piedra
          [p] papel
          [t] tijera
          [x] salir
          '''))
    if player1 == 's':
      if playerPC == 'piedra':
        print('¡Fue un empate!')
      elif playerPC == 'papel':
        print('¡Perdiste!')
        ptoPlayerPC += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}:'.format(nombre),ptoPlayer1)
      elif playerPC == 'tijera':
        print('¡Felicidades, ganaste!')
        ptoPlayer1 += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}: '.format(nombre),ptoPlayer1)

    elif player1 == 'p':
      if playerPC == 'piedra':
        print('¡Felicidades, ganaste!')
        ptoPlayer1 += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}: '.format(nombre),ptoPlayer1)
      elif playerPC == 'papel':
        print('¡Fue un empate!')
      elif playerPC == 'tijera':
        print('¡Perdiste!')
        ptoPlayerPC += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}: '.format(nombre),ptoPlayer1)

    elif player1 == 't':
      if playerPC == 'piedra':
        print('¡Perdiste!')
        ptoPlayerPC += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}: '.format(nombre),ptoPlayer1)
      elif playerPC == 'papel':
        print('¡Felicidades, ganaste!')
        ptoPlayer1 += 1
        print('Punto de la PC: ', ptoPlayerPC)
        print('Puntos de {}: '.format(nombre),ptoPlayer1)
      elif playerPC == 'tijera':
        print('¡Fue un empate!')

    elif player1 == 'x':
      break

    else:
      print('Opción no válida.')


def run():

  while True:

    print('=====================')
    print('*       JUEGO       *')
    print('=====================')
    print('Hola {} '.format(nombre))
    opcion = str(input('''
          ¿Qué deseas hacer?
          [g] jugar
          [s] salir
          '''))
    if opcion == 'g':
      game()
    elif opcion == 's':
      break
    else:
      print('Opción no válida.')


if __name__ == '__main__':
  nombre = input('Dime tu nombre: ')
  run()