n1 = float(input('Primeira nota do aulo e: '))
n2 = float(input('Segunda nota do aulo e: '))
n3 = float(input('Terceira nota do aulo e: '))
n4 = float(input('Quarta nota do aulo e: '))

soma = n1 + n2 + n3 + n4
divisao = soma / 4

if divisao<7.0:
    print(f'A média é {divisao} e infelizmente o aluno esta retido :(')
else:
    print(f'A media e {divisao} e aluno esta promovido ao proximo ano::)')
