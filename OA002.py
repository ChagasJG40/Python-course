n1 = int(input('Digite o primeiro nº:'))
n2 = int(input('Digite o segundo nº:'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('O valor da soma {}, a subtração é {} e a multiplicação é {}'.format(s, su, m), end='')

print('O valor da divisão é {:.3f}, do exponencial é {}, da divisão inteira é {}, e do resto da divisão é {}'.format(d, e, di, rd))
