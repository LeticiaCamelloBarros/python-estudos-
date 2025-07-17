numero = int(input())
lista_de_numeros_pares = []
lista_de_numeros_impares = []
for i in range(numero):
    if i % 2 == 0:
        #    se i for par
        lista_de_numeros_pares.append(i)
    else:
        lista_de_numeros_impares.append(i)


print(f" os numeros impares são {lista_de_numeros_impares}")
print(f"os numeros pares são {lista_de_numeros_pares}")
