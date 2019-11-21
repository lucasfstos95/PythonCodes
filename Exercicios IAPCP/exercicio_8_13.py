#Exercicio 8.13 - 

def validar(S):
    l = S.lower()
    l = list(l)
    op = input("Digite uma caracter como opção: ").lower()
    if op in l:
        print("Opção válida!")
    else:
        print("Opção inválida!")
        validar(S)

s = input("Digite uma string: ")
validar(s)