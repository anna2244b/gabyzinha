ilha1 = input('Emma - ei, capitão!, Aquilo alí parece uma ilha. devemos parar o navio? sim/não')
while True:
 if ilha1 == 'sim':
  print('PIRATAS!. vamos procurar comidas mantimentos armas etc... NÃO SE SEPAREM OK? piratas- SIM SENHOR CAPITÃO!!!!.')
 else:
  print('*tempestade*')
 from random import randint
 tempestade = randint(0, 3)
 if tempestade == '2':
   print('Oops! you died.')
 break