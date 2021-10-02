N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

average = (N1*2 + N2*3 + N3*4 + N4)/10.0

print('Media: {:.1f}'.format(average))

if average >= 7:
    print('Aluno aprovado.')
elif average < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota = float(input())
    print('Nota do exame: {:.1f}'.format(nota))
    faverage = (average + nota)/2.0
    if faverage >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(faverage))