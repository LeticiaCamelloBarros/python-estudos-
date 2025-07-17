lado = int(input("insira o tamanho do lado do quadrado "))

var_largura_vazio = " " * (lado-2)
# variável para guardar a impressão do espaço vazio de cada linha
var_largura_vazio_e_hastag = "#"+var_largura_vazio+"#"
# variável para guardar a impressão dos espaços vazios de cada linha e
#  da hastag que fica antes e depois da sequencia de espaços vazios de cada linha
print("#"*lado)
# printar  primeira linha que vai ser só hastag
for i in range(lado-2):
    print(var_largura_vazio_e_hastag)
    # esse laço for vai servir para printar lado - 2 vezes linhas que começam com hastag ,
    # terminam com hastag mas que entre esses dois hastags há uma sequencia de lado-2 espaços vazios
print("#"*lado)
# printar a ultima linha que também será só de hastag
