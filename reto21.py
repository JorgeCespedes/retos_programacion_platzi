CO = 100
i = 4

def run():
  
  while True:
    print('')
    print('Conoce el importe de tu ahorro')
    op = input('''
        Escoge una opción:
        [1] A seis meses
        [2] A un año.
        [3] A dos años
        [x] Salir
        ''')
    
    if op == '1':
      tiempo = 6
      calculo_de_ahorro(tiempo)

    elif op == '2':
      tiempo = 12
      calculo_de_ahorro(tiempo)
    
    elif op == '3':
      tiempo = 24
      calculo_de_ahorro(tiempo)
    
    elif op == 'x':
      break
    
    else:
      print('Opción no válida')


def calculo_de_ahorro(tiempo):
  I_ganado =  round( (CO * ( (pow(1 + (i/100), tiempo) ) - 1)),2 )
  
  print('Importe ahorrado (USD): {} '. format(CO))
  print('Interés ganado (USD): {}'. format(I_ganado))
  print('Total ganado (USD): {}'. format(CO + I_ganado))
  print('Periodo de ahorro: {} meses'. format(tiempo))


if __name__ == '__main__':
  run()