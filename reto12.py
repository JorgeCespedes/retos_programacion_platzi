from datetime import date
from datetime import datetime
from datetime import timedelta

today = date.today()

def calcula_dias_faltantes(fecha):
  dias_faltantes = fecha - today
  print('Faltan ', dias_faltantes, 'dias para tu próximo cumpelaños.')

def run():
  fecha = str(input('Ingresa la fecha de tu cumpleaños. yyyy-mm-dd: '))
  fecha = date.fromisoformat(fecha)
  new_fecha = date(today.year, fecha.month, fecha.day)
  calcula_dias_faltantes(new_fecha)

if __name__ == '__main__':
  run()