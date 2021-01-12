def areaTriangulo(b,h):
  area = (b * h) / 2
  return print('El area del trinagulo es: ', area)

def tipoTriangulo(l1,l2,l3):
  if (l1 != l2 and l1 != l3 and l2 != l3):
    print('Triangulo escaleno.')
  elif (l1 == l2 and l1 == l3 and l2 == l3):
    print('Triangulo equilatero.')
  else:
    print('Triangulo isoseles.')

def run():
  while True:
    opcion = input('''
          Qué deseas hacer:
          [a] area triangulo
          [b] tipo triangulo
          [s] salir
                  ''')

    if opcion == 'a':
        base = int(input('Ingresa la base: '))
        altura = int(input('Ingresa la altura: '))
        area = areaTriangulo(base, altura)
    elif opcion == 'b':
      lado1 = int(input('Ingresa el lado 1: '))
      lado2 = int(input('Ingresa el lado 2: '))
      lado3 = int(input('Ingresa el lafo 3: '))
      tipoTriangulo(lado1, lado2, lado3)
    elif opcion == 's':
      break
    else:
      print('Opcion no válida. Intentalo de nuevo.')

if __name__ == '__main__':
  run()