InitialTime , EndTime = input().split()

InitialTime = int(InitialTime)
EndTime = int(EndTime)

if EndTime == InitialTime:
    print("O JOGO DUROU 24 HORA(S)")
else:
    aux = 0
    while EndTime != InitialTime:
        if EndTime == 0 and InitialTime != 0:
            EndTime = 24
        EndTime = EndTime - 1
        aux = aux + 1
    print("O JOGO DUROU {} HORA(S)".format(aux))