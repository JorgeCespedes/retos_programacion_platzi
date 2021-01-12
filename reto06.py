
def operaciones(n1,n2, op):
  if op == '+':
    print('La operación es: ', n1 + n2)
  elif op == '-':
    print('La operación es: ', n1 - n2)
  elif op == '*':
    print('La operación es: ', n1 * n2)
  elif op == '/':
    if n2 != 0:
      print('La operación es: ', n1 / n2)
    else:
      print('No se puede dividir entre cero.')


if __name__ == '__main__':
  numero1 = int(input('Numero 1: '))
  numero2 = int(input('Numero 2: '))
  tipo_operacion = str(input('Tipo de operación a realizar :+,-,*,/ : '))
  operaciones(numero1,numero2, tipo_operacion)