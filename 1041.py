X, Y = input().split()

X = float(X)
Y = float(Y)

if X == 0 and Y == 0:
    print('Origem')
if X == 0 and Y != 0:
    print ('Eixo Y')
if X != 0 and Y == 0:
    print('Eixo X')
if X > 0 and Y > 0:
    print('Q1')
if X > 0 and Y < 0:
    print('Q4')
if X < 0 and Y > 0:
    print('Q2')
if X < 0 and Y < 0:
    print('Q3')