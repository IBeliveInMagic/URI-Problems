x, y, z = input().split()

x = int(x)
y = int(y)
z = int(z)

if x >= y and x >= z:
    greatest = x
elif y >= x and y >= z:
    greatest = y
elif z >= x and z >= y:
    greatest = z

print('{} eh o maior'.format(greatest))