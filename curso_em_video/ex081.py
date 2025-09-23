valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    rsp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if rsp in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} valores na lista.')
valores.sort(reverse=True) # deixa de forma decrecente
print(f'Lista ordenada de forma decrescente {valores}.')
if 5 in valores:
    print('O valor 5 esta na lista.')
else:
    print('O numero 5 não esta na lista.')
