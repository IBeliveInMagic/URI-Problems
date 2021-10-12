sides = []

sides = [float(i) for i in input().split()]

#decreasing order
sides.sort(reverse=True)

A = sides[0]
B = sides[1]
C = sides[2]

aux = 0

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A*A == (B*B + C*C):
        print("TRIANGULO RETANGULO")
    if A*A > (B*B + C*C):
        print("TRIANGULO OBTUSANGULO")
    if A*A < (B*B + C*C):
        print("TRIANGULO ACUTANGULO")
    if (A == B) and (B == C):
        print("TRIANGULO EQUILATERO")
        aux = 1
    if aux != 1:
        if ((A == B) and (A != C)) or ((A == C) and (A != B)) or ((B == C) and (B != A)):
            print("TRIANGULO ISOSCELES")