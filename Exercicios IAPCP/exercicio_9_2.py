#Exercício 9.2- Manipulando arquivos pelo terminal selecionando linhas
import sys

nome_arquivo = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3])

with open(nome_arquivo, 'r') as arquivo:
    lista = arquivo.readlines().copy()
    for linha in range(inicio, fim+1):
        print(lista[linha], end="")