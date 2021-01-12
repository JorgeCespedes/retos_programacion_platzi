import math

PI = math.pi

def superficieLateral(radio, altura):
  supLateral = (2*PI*radio) * altura
  supLateral = round(supLateral,1)
  print('La superficie lateral del cilindo: {}'.format(supLateral))

def volumenCilinro(radio, altura):
  vol = PI * math.pow(radio,3)*altura
  vol = round(vol,1)
  print('El volumen es: {}'.format(vol))

if __name__ == '__main__':
  print('Programa para el volumen de un cilindro:')
  radio = int(input('Ingresa el radio de la base: '))
  altura = int(input('Ingresa la altura: '))

  volumenCilinro(radio, altura)
  superficieLateral(radio, altura)