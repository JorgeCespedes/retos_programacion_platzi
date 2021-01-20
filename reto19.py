import random



def posicion_inicial(character):
  for x in character:
    indice = character.index(x)
    print('Posicion {} del símbolo: {} '. format(indice, x))
    

def seleccion_aleatoria(character):
  for i in range(4):
    aleatorio = random.randint(0,len(character) - 1)
    simbolo = character[aleatorio]
    memory.append(simbolo)
    resultado = ''.join(memory)
    print('El símbolo {} corresponde a la posición: {} '. format(simbolo, aleatorio))
    
  print('Se escogieron los siguiens símbolos: ',resultado)

if __name__ == "__main__":
  character = '"#$%()/&'
  memory = []
  seleccion_aleatoria(character)
  print('-'*15)
  
  posicion_inicial(character)