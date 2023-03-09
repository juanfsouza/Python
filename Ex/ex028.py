from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 tente adivinhar...')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei? '))
print('PROCESSANDO....')
sleep(3)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('IA: GANHEI! Voce muito ruim nao sabe o que estou pensando...')