numero = int(input())
lista_de_divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        lista_de_divisores.append(i)

# print(lista_de_divisores) // etapa que serve meramente para verificar se as et
if len(lista_de_divisores) <= 2:
    # nesse caso o número só será divisível por um e por ele mesmo 
    print("esse numero é primo ")
else:
    print("esse número não é primo ")
