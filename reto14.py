  def es_primo(numero):
    if numero < 2:
      return False
    for i in range(2, numero):
      if numero % i == 0:
        return False
    return True


  def lista_numeros_primos(limite):
    contador = 0
    i = 0
    while contador < limite:
      i += 1
      if es_primo(i):
        contador += 1
        print(i)


  def run():
    print(" == Listado de número primos == ")
    limite = int(input('Ingresa el límite de números primos: '))
    lista_numeros_primos(limite)

  if __name__ == '__main__':
    run()