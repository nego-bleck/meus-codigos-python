valores = []
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    rsp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if rsp == 'N':
        break

for v in valores: # pecorre a lista 
    if v % 2 == 0:
        listaPar.append(v) # adiciona por
    elif v % 2 == 1:
        listaImpar.append(v) # adiciona ímpar

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {listaPar}')
print(f'A lista dos numeros impares é {listaImpar}')
