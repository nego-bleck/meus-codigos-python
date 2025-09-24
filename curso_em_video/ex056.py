somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = 0
totmulher20 =0
for p in range(1, 5):
    print(f'-----{p}º PESSOA-----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if p == 1 and sexo in 'Mn':
        maioridadehome = idade
    if sexo in 'Mn' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
    somaidade += + idade
mediaidade = somaidade / 4
print(f'A média da idade do grupo é {mediaidade}')
print(f'O homen mas velho tem {maioridadehome} e se chame {nomevelho} ')
print(f'Ao todo são {totmulher20} tantas mulher com  menos de 20 anos')

