print("insira um valor válido sabendo que para ser válido deve estar compreendido no intervalo entre 0 e 10 ")
nota = int(input("Qual foi a sua nota ? "))

valid = False
while (valid == False):
    nota = int(input("Qual foi a sua nota ? "))
    if 0 <= nota >= 10:
        valid = True
