n1 = float(input('digite um numero para a largura da parede: '))
n2 = float(input('digite um numero para a altura da parede: '))

area = n1 + n2

if area > 10.0:
    print(f'Sua parede tem a dimensao de {n1}x{n2} a sua area e de {area}²')
    print(f'voce tem tinta suficiente para pintar a parede toda')
else:
    print(f'Sua parede tem a dimensao de {n1}x{n2} a sua area e de {area}²')
    print(f'Voce nao tem tinta suficiente para pintar a parede, para pintar a parede voce precisaria de 10.0²')
