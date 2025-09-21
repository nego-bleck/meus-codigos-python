valores = []
while True:
    nun = int(input('Digite um valor: '))

    if nun in valores:
        print('Valor duplicado na lista, Não vou adicionar...')
    else:
        valores.append(nun)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Valores cadastrados {valores}')

