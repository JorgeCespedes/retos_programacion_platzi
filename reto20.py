import random

def posicion_inicial(character):
  for x in character:
    indice = character.index(x)
    print('  Posicion {} del símbolo: {} '. format(indice, x))
    

def seleccion_de_usuario(character, limite_simbolo):
  posicion_inicial(character)
  memory = []
  for i in range(limite_simbolo):
    indice_simbolo = int(input('Selecciona el índice: '))
    simbolo = character[indice_simbolo]
    memory.append(simbolo)
    resultado = ''.join(memory)

  print('Escogiste los símbolos: {}'. format(resultado))

if __name__ == "__main__":
  character = '"#$%()/&'
  
  print('Escoga los símbolos que más te gustan')
  print('Marque el número para escoger:')
  
  limite_simbolo = int(input('Cuántos símbolos quieres : '))
  
  print('-'*15)

  seleccion_de_usuario(character, limite_simbolo)  