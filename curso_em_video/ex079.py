valores = [] #lista vazia
while True:
    nun = int(input('Digite um valor: '))

    if nun in valores: # verifica se o numero ta na lista
        print('Valor duplicado na lista, Não vou adicionar...')
    else:
        valores.append(nun) # adiciona numero na lista
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN': # pergunta se quer continuar, nao aceita outro caracter
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort() # ordena a liata de forma crecente 
print('-=' * 30)
print(f'Valores cadastrados {valores}')

