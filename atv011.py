Dias = int(input('Quantos dias esteve alugado?:'))
km = float(input('Quantos quilometros foram rodados'))
Vpd = (Dias * 60) + (km * 0.15)
print('O Valor total a pagar R${:.2F}'.format(Vpd))
