

def run():
  CO = int(input('Ingresa el importe que deseas ahorrar: '))
  tiempo = int(input('Escoge el número de meses para ahorrar: '))
  
  
  tasa = 4
  calculo_de_ahorro(tiempo, CO, tasa)
  
  tasa = 3
  calculo_de_ahorro(tiempo, CO, tasa)

def calculo_de_ahorro(tiempo,CO, tasa):
  I_ganado =  round( (CO * ( (pow(1 + (tasa/100), tiempo) ) - 1)),2 )
  
  print('')
  print(' -- RESUMEN DE ESTADO -- ')
  print('Importe ahorrado (USD): {} '. format(CO))
  print('Interés ganado (USD): {}'. format(I_ganado))
  print('Total ganado (USD): {}'. format(CO + I_ganado))
  print('Periodo de ahorro: {} meses'. format(tiempo))
  print('Tasa: {} %'. format(tasa))


if __name__ == '__main__':
  run()
  print('Banco Alternativo')