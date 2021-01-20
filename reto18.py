import random

character = '"#$%()/&'
memory = []

for i in range(4):
  simbolo = character[random.randint(0,len(character))-1]
  memory.append(simbolo)
  resultado = ''.join(memory)
  
print(resultado)
