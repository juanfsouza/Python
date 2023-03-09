num = float(input('Qual é o preço do produto? R$'))

desconto = num*5/100
resultado = num - desconto

print(f' O produto ques custava R$ {num}, na promoçao com desconto de 5% vai custa R${resultado}')