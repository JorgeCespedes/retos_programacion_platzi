import csv

with open('nombres.csv', 'r') as file_handle:
  leer_archivo = csv.reader(file_handle)
  for line in leer_archivo:
    print(line)



'''
with open("nombres.csv", newline="") as csvfile:
  snf = csv.Sniffer()
  reader = csv.reader(csvfile, delimiter=",")
  for row in reader:
    print(row)
    #print(row['nom'])
'''