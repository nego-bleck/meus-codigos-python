sexo = str(input('Informe seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalido. Por favro, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
