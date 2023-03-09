nome = str(input('Digite seu nome completo: ')).strip()
print('muito prazer em te conhecer!')

primeiro = nome.split()

print(f'Seu primeiro nome e {primeiro[0]}')
print(f'Seu ultimo nome e {nome.split()[-1]}')