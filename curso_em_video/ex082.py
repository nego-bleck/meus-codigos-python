valores = []
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    rsp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if rsp == 'N':
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {listaPar}')
print(f'A lista dos numeros impares é {listaImpar}')
