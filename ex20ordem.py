import random
n1 = str(input('Digite aluno 1:'))
n2 = str(input('Digite aluno 2:'))
n3 = str(input('Digite aluno 3:'))
n4 = str(input('Digite aluno 4:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação do trabalho será:')
print(lista)