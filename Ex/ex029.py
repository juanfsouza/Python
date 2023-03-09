carro = float(input('Qual era sua velocidade do carro? '))

multa = (carro - 80) * 7


if carro > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80km/h')
    print(f'Voce foi multado em R${multa}')
else:
    print(f'Sua velociade e de {carro}km/h voce nao foi multado dirigia com segurança')