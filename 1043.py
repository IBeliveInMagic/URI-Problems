A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

if (abs(B - C)  < A and A < B + C) and (abs(A - C) < B and B < A + C) and (abs(A - B) < C and C < A + B):
    print('Perimetro = {:.1f}'.format(A +B +C))
else:
    print('Area = {:.1f}'.format(((A + B)*C)/2.0))
