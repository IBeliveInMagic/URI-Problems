original = []
sortarray = []

original = [int(i) for i in input().split()]
sortarray = original.copy()

sortarray.sort()

for i in range(0,len(sortarray)):
    print(sortarray[i])
print()
for i in range(0,len(original)):
    print(original[i])