import math

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

Delta = (B*B) - (4*A*C)

if A == 0 or Delta < 0:
    print('Impossivel calcular') 
else:
    x1 = (-B + math.sqrt(Delta))/(2*A)
    x2 = (-B - math.sqrt(Delta))/(2*A)

    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))