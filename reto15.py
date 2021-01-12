#Calculadora de volúmenes Cilindro, Cubo, Esfera
import math

PI = math.pi

def volumenCilinro(radio, altura):
  vol = PI * math.pow(radio,3)*altura
  vol = round(vol,1)
  print('Volumen cilindro: {}'.format(vol))

def volumenCubo(lado):
  vol = math.pow(lado,3)
  vol = round(vol,1)
  print('Volumen Cubo: {}'.format(vol))

def volumenEsfera(radio):
  vol = (4/3) * PI * (math.pow(radio,3))
  vol = round(vol,1)
  print('Volumen esfera: {}'.format(vol))


def run():
  while True:
    opcion = int(input('''
            ¿Qué deseas calcular?
            [1] Volumen de un cilindro
            [2] Volumen de un Cubo
            [3] Volumen de una Esfera
            [4] Salir
            '''
            ))
    if opcion == 1:
      radio = int(input('Ingresa el radio de la base: '))
      altura = int(input('Ingresa la altura: '))
      volumenCilinro(radio, altura)

    elif opcion == 2:
      lado = int(input('Ingresa la medida del lado: '))
      volumenCubo(lado)

    elif opcion == 3:
      radio = int(input('Ingresa el radio de la esfera: '))
      volumenCubo(radio)

    elif opcion == 4:
      break

    else:
      print('Opción no válida.')


if __name__ == '__main__':
  run()

