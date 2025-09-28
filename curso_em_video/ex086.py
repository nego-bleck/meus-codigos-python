matriz = [[0,0,0], [0,0,0], [0,0,0]] # matris 3x3
#for linha e coluna de alimentação
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
# for para mostra resultado na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()