print('='*30)
print('10 TERMOS DA UMA PA')
print('='*30)

primerito = int(input("Primeiro termo: "))
razao = int(input('Razão:'))
decimo = primerito + (10 - 1) * razao
for c in range(primerito, decimo + razao, razao):
    print(f'{c}',end= ' -> ')
print('ACABOU')
