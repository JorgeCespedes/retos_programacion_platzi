def calulaSegundos(h,m):
  segPorMinutos = 60
  segPorHora = 60*60
  total_segundos = h*segPorHora + m * segPorMinutos
  print(total_segundos)

if __name__ == '__main__':
  hora = int(input('Ingresa el número de horas: '))
  minuto = int(input('Ingresa el numero de minutos: '))
  calulaSegundos(hora, minuto)