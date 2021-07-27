
dia = input('oi!! tudo bem?, que dia da semana é hoje?')
if dia == 'terça' or 'sexta':
    print('eitaa!, hoje é dia de promoção!, vai aproveita não é? aproveita pra estourar o cartão!!')
preços = 19
promoçao = preços * 0.4
valorpago = preços * 0.60
carrinho = input('finalizar carrinho?')
if carrinho == 'sim':
    print('valor com desconto: {}'.format(valorpago))