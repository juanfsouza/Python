import math
num = int(input('Digite o angulo que voce deseja: '))

seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))

print(f'O angulo de {num} tem o SENO de {seno}')
print(f'O angulo de {num} tem o COSSENO de {cosseno}')
print(f'O angulo de {num} tem o TANGENTE de {tangente}')