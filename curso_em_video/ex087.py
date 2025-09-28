matriz = [[0,0,0], [0,0,0], [0,0,0]] # matris 3x3
par = maior = soma = 0
#for linha e coluna de alimentação
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        # verifica se é par e guarda
        if matriz [l][c] % 2 == 0:
            par += matriz [l][c]

print('-='*30)
# for para mostra resultado na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {par}')

