VOCALS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó', 'ú']

parrafo = str(input('Ingresa un párrafo: '))


for vocal in VOCALS:
  parrafo = parrafo.replace(vocal, ' ')
print(parrafo)