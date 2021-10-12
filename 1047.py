InitialHour, InitialMinute, EndHour, EndMinute = input().split()

InitialHour = int(InitialHour)
InitialMinute = int(InitialMinute)
EndHour = int(EndHour)
EndMinute = int(EndMinute)

if InitialHour == EndHour and InitialMinute == EndMinute:
    auxHour = 24
    auxMinute = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(auxHour,auxMinute))
else:
    auxHour = 0
    if InitialHour == EndHour and InitialMinute > EndMinute:
        auxHour = 24
    else:
        while EndHour != InitialHour:
            if EndHour == 0 and InitialHour != 0:
                EndHour = 24
            EndHour = EndHour - 1
            auxHour = auxHour + 1
    auxMinute = 0
    while EndMinute != InitialMinute:
        if EndMinute == 0 and InitialMinute != 0:
            EndMinute = 60
            auxHour = auxHour - 1
        EndMinute = EndMinute - 1
        auxMinute = auxMinute + 1
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(auxHour,auxMinute))