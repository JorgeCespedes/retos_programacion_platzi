def repetimos(f,v):
  if v == 1:
    print(f)
  else:
    return print(f*v)

if __name__ == '__main__':
  frase = str(input('Dinos algo: '))
  veces = int(input('Cuantas veces lo repetimos: '))
  repetimos(frase,veces)
