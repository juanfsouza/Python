num = int(input('Digite um numero: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

milhar = int(milhar)
dezena = int(dezena)
centena = int(centena)

print(f'analisando numero {num}')
print(f'unidade {unidade}')
print(f'dezena {dezena}')
print(f'centena {centena}')
print(f'milhar {milhar}')