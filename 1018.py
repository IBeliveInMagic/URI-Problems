notes = int(input())

print(notes)

list = [100,50,20,10,5,2,1]

for i in list:
    print('{} nota(s) de R$ {},00'.format(notes//i, i))
    notes = notes % i