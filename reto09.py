import random

numero_aleatorio = random.randint(0, 100)

print(numero_aleatorio)

def adivina_el_numero(numero):
  intentos = 0
  while True:
    if numero > numero_aleatorio:
      print('El número que buscas es menor. ')
      numero = int(input('Ingresa un numero: '))
      intentos += 1
    elif numero < numero_aleatorio:
      print('El número que buscas es mayor. ')
      numero = int(input('Ingresa un numero: '))
      intentos += 1
    elif numero == numero_aleatorio:
      print('Feliciades, ¡acertaste!')
      break
  print('Intentos realizados: {}'.format(intentos))


if __name__ == '__main__':
  print('Adivina el numero entre 0 y 100')
  numero = int(input('Ingresa un numero: '))
  adivina_el_numero(numero)
