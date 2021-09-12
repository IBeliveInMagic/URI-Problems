pi = 3.14159

A, B, C = input().split()

triangle = float(A)*float(C)/2
circle = pi*float(C)*float(C)
trapezium = ((float(A)+float(B))*float(C))/2
square = float(B)*float(B)
rectangle = float(A)*float(B)

print('TRIANGULO: {:.3f}'.format(triangle))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapezium))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))
