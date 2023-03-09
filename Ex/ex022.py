nome = str(input('Digite seu nome inteiro: '))

maior = nome.upper()
menor = nome.lower()
sem = len(nome)-nome.count(' ')
primeiro = nome.split()


print(f'Seu nome com letras maiusculas: {maior}')
print(f'Seu nome com letras minusculas: {menor}')
print(f'Seu nome em numeros contados: {sem}')
print(f'Seu nome so o primeiro nome : {primeiro[0]}')