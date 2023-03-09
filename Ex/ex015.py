alugado = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

valor = alugado * 60
rodado = km * 0.15
resultado = valor + rodado

print(f'O total a pagar e de R${resultado}')