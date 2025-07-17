numero = int(input())
lista_de_divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        lista_de_divisores.append(i)

print(lista_de_divisores)
if len(lista_de_divisores) <= 2:
    print("esse numero é primo ")
else:
    print("esse número não é primo ")
