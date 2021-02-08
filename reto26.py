import csv

archivo_nombres = open('nombres.csv', 'r')

header = archivo_nombres.readline()

reader = csv.reader(archivo_nombres)
reader = sorted(reader)


for linea in reader:
  print(linea[0])
  