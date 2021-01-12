
VOCALS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó', 'ú']

def conversorPalabra(palabra):
  for vocal in VOCALS:
    if palabra[0] == vocal:
      palabra = palabra + 'way'
      return palabra
    else:
      palabra = palabra[1:] + palabra[0] + 'ay'
      return palabra


if __name__ == '__main__':
  print('Este idioma se llama Pig Latin')
  palabra = str(input('Ingresa una palabra para traducirla: '))
  PigLatin = conversorPalabra(palabra)
  print('La palabra', palabra, 'se traduce como: ',PigLatin)
