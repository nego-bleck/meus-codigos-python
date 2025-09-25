pessoas = []
dados = []
mai = men = 0

while True:

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:]) # copia os dados para a lista principal

    dados.clear() # limpa para não misturar os próximos cadastros
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Foram cadastratas {len(pessoas)} pessoas')
print(f'O maior pese foi de {mai} KG', end=' ')
for p in pessoas: #laço para pecorrer a lisra e trocar os valores
    if p[1] == mai:
        print(f'[{p[0]}', end=' ')
print()
print(f'O menor peso foi de {men} KG', end=' ')
for p in pessoas:
    if p [1] == men:
        print(f'[{p[0]}] ', end=' ')
