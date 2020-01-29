#Exercício 9.1- Manipulando arquivos pelo terminal
import sys

nome_arquivo = sys.argv[1]

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha, end="")