X, Y = input().split()

X = int(X)
Y = int(Y)

V = [4.00, 4.50, 5.00, 2.00, 1.50]

print('Total: R$ {:.2f}'.format(V[X-1]*Y))