n1 = float(input('digite um numero para a largura da parede: '))
n2 = float(input('digite um numero para a altura da parede: '))

resultado = (n1 + n2) * 2
falta = (n1 + n2) / 2

print(f'Sua parede tem a dimensao de {n1}x{n2} a sua area e de {resultado}')
print(f'Para pintar essa parede, voce precisara de {falta} de tinta')