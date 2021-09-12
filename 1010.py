code1, units1, price1 = input().split()

code2, units2, price2 = input().split()

value1 = int(units1)*float(price1)
value2 = int(units2)*float(price2)

print('VALOR A PAGAR: R$ {:.2f}'.format(value1+value2))