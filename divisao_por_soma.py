"""
Faça um algoritmo que realize a divisão entre dois números dados pelo usuário
utilizando apenas a operação de soma.
"""
try_again = True
while (try_again):
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    sum = n2
    qtd_sum = 0
    while (sum <= n1):
        sum = sum + n2
        qtd_sum = qtd_sum + 1
        print(f'divisor = {sum}, qtd = {qtd_sum}, resto = {sum-n1}')

    print(f'{n1}/{n2} = divisor {qtd_sum}, resto {sum-n1}')

    option = input('Deseja calcular novamente? [S/N]')
    if option == 'N' or option == 'n':
        try_again = False
