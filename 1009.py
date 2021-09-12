nome = input()
fixo = float(input())
vendas = float(input())

bonus = (15*vendas)/100

print('TOTAL = R$ {:.2f}'.format(fixo + bonus))