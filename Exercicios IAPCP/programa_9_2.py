#Programa 9.2 - uso do with
with open("arquivos/numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)