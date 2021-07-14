from random import randint
mapa: print('.......................ilha muaca...............pedras.................muca............'
               '............................ilha jungue......x')

def mapa():
 print(mapa)
ilha1 = input('Emma - ei, capitão!, Aquilo alí parece uma ilha. devemos parar o navio? sim/não')
while True:
 if ilha1 == 'sim':
  print('PIRATAS!. vamos procurar comidas mantimentos armas etc... NÃO SE SEPAREM OK? piratas- SIM SENHOR CAPITÃO!!!!.')
  monstro = 1
  usuario = input('digite um numero de 1 a 12: ')
  if usuario <= monstro:
   print('fugimos.. uou oque È isso parece um mapa')
   pegar = input('pegar mapa')
   if pegar == 'sim':
    mapa()
    print('voltar para navio')
   elif pegar == 'não':
     print('pegue o mapa!')
  else:
   print('opss!you died.')
 else:
  print('Seu navio entrou em uma grande tempestade')
 tempestade = randint(0, 3)
 if tempestade == '2':
   print('Oops! you died.')
 else:
  print('vc escapou')

 break