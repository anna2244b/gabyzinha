from random import  randint
numero = randint(0, 10)
tentativas = 0
while True:
  jogador = int(input('Digite um número de 0 a 10 '))
  if jogador == numero:
     print('Parabéns, você acertou meu número!')
  if jogador > numero:
     print('opa! número muito grande. Tente um numero menor')
  tentativas += 1
  if jogador < numero:
    print('ei esse número è muito pequeno. Tente um número maior')
print('tentativas: {}'.format(tentativas))
