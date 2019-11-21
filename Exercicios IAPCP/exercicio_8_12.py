#Exercicio 8.12 - busca string em lista

def buscaStr(S, L):
    L = "".join(L)
    if not(L.find(S) == -1):
        return True
    else:
        return False

L = ['l', 'u', 'c', 'a', 's', ' ', 'f', 'e', 'l', 'i', 'p', 'e']
s = input("Digite uma string: ")

print(f"{s} está em {L}? {buscaStr(s, L)}")

