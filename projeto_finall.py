ilha1 = input('Emma - ei, capitão!, Aquilo alí parece uma ilha. devemos parar o navio? sim/não')
while True:
 if ilha1 == 'sim':
  print('PIRATAS!. vamos procurar comidas mantimentos armas etc... NÃO SE SEPAREM OK? piratas- SIM SENHOR CAPITÃO!!!!.')
  monstro = 11
  usuario = input('digite um numero de 1 a 12: ')
  if usuario <= monstro:
   print('voce achou o mapa')
     print('voltar para navio')
  else:
   print('opss!you died.')
 else:
  print('Seu navio entrou em uma grande tempestade')
 tempestade = from random import randint(0, 3)
 if tempestade == '2':
   print('Oops! you died.')
 else:
  print('vc escapou')
 break