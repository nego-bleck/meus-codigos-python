
num = [[], []] # lista composra
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: ')) #
    if valor % 2 == 0:
        num[0].append(valor) # adiciona dentro a lista composta a lista de par
    else:
        num[1].append(valor) # adiciona dentro a lista composta a lista de impar
# usando o atributo sorted na saida para colocar em ordem crecente
print('-='*30)
print(f'Os valores pares digitados foram {sorted(num[0])}')
print(f'Os valores impares digitados foram {sorted(num[1])}')
