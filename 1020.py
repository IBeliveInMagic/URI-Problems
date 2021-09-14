N = int(input())

year = N//365
N = N%365
months = N//30
days = N%30

print('{} ano(s)'.format(year))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))