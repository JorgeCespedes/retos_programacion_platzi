import random

def ordena_numeros(lista_numeros):
  lista_numeros.sort()
  return lista_numeros

if __name__ == "__main__":
  lista_numeros =  [random.randint(0,100) for x in range(10)]
  print(lista_numeros)
  
  lista_ordenada = ordena_numeros(lista_numeros)
  print(lista_ordenada)