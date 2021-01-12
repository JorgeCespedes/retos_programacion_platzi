import random

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p','q','r','s','t', 'u','v','w','x','y','z']
mayusculas = [ele.upper() for ele in minusculas]
simbolo = ['*', '+', '-', '/','#', '@','%', '&', '(', ')', '?','!']
numeros = ['1', '2','3','4','5','6','7','8','9','0']


def generar_password_minusculas(numero_de_caracteres):
  caracteres =  minusculas
  password = []
  for i in range(numero_de_caracteres):
    caracter_randon = random.choice(caracteres)
    password.append(caracter_randon)
  password = ''.join(password)
  return password

def  generar_password_mayusculas(numero_de_caracteres):
  caracteres =  minusculas + mayusculas
  password = []
  for i in range(numero_de_caracteres):
    caracter_randon = random.choice(caracteres)
    password.append(caracter_randon)
  password = ''.join(password)
  return password

def  generar_password_numeros(numero_de_caracteres):
  caracteres =  minusculas + mayusculas + numeros
  password = []
  for i in range(numero_de_caracteres):
    caracter_randon = random.choice(caracteres)
    password.append(caracter_randon)
  password = ''.join(password)
  return password

def generar_password_simbolos(numero_de_caracteres):
  caracteres =  minusculas + mayusculas + numeros + simbolo
  password = []
  for i in range(numero_de_caracteres):
    caracter_randon = random.choice(caracteres)
    password.append(caracter_randon)
  password = ''.join(password)
  return password


def run():
  while True:
    opcion = str(input('''
          Escoja una opción:
          [n] Solo minusculas.
          [m] Incluye mayusculas.
          [nu] Incluye numeros.
          [ce] Incluye caracteres especiales.
          [x] Salir.
          '''
          ))
    if opcion == 'n':
      numero_de_caracteres = int(input('Cuantos caracteres quieres que tenga tu passeord: '))
      password = generar_password_minusculas(numero_de_caracteres)

    elif opcion == 'm':
      numero_de_caracteres = int(input('Cuantos caracteres quieres que tenga tu passeord: '))
      password = generar_password_mayusculas(numero_de_caracteres)

    elif opcion == 'nu':
      numero_de_caracteres = int(input('Cuantos caracteres quieres que tenga tu passeord: '))
      password = generar_password_numeros(numero_de_caracteres)

    elif opcion == 'ce':
      numero_de_caracteres = int(input('Cuantos caracteres quieres que tenga tu passeord: '))
      password = generar_password_simbolos(numero_de_caracteres)

    elif opcion == 'x':
      break

    else:
      print('Opcion no válida. Vuelve a intentarlo.')

    print('Tu contraseña es: ' + password)


if __name__ == '__main__':
  run()

