preço = float(input('Qual é o preço do produto R$ '))
desconto = preço - (preço * 5 /100)
print('O valor do produto com 5% de desconto é de R${:.2f}'.format(desconto))