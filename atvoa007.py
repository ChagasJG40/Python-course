largura = int(input('Digite a largura em metros:'))
altura = int(input('Digite a altura em metros:'))
area = largura * altura
tinta = area / 2 ** 2
print('A área a ser pintada é de {} metros quadrados, e a quantidade de tinta a ser utilizada é de {} latas'.format(area, tinta))
