value = float(input())

notes = [100,50,20,10,5,2]
coins = [1,0.50,0.25,0.10,0.05,0.01]

print("NOTAS:")
for i in notes:
    print('{} nota(s) de R$ {:.2f}'.format(int(value/i), i))
    value = round(value % i,2)

print("MOEDAS:")
for i in coins:
    print('{} moeda(s) de R$ {:.2f}'.format(int(value/i), i))
    value = round(value % i,2)