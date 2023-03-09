nome = str(input('Digite uma frase: ')).strip()

print(f'Sua frase possui {nome.lower().count("a")} letras A ')
print(f'A primeira letra A apareceu na posiçao {nome.lower().find("a")+1}')
print(f'A primeira letra A apareceu na posiçao {nome.lower().rfind("a")+1}')