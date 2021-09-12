import math

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

X = x2 - x1
Y = y2 - y1


distance = math.sqrt((X*X) + (Y*Y)) 

print('{:.4f}'.format(distance))