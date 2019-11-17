#Exercício 6.9 funciona para o 6.10 - Pesquisa
L = [17,7,27,39]
p = int(input("Digite o 1º valor a procurar: "))
v = int(input("Digite o 2º valor a procurar: "))
achou = False
x=0
i=0
pPos=-1
vPos=-1
while x < len(L):
    if L[x] == p:
        pPos = x
        achou = True
    elif L[x] == v:
        vPos = x
        achou = True
    elif vPos != -1 and pPos != -1:
        achou = True
        break
    x += 1

if pPos > vPos and vPos == -1:
    print(f"{p} encontrado em {pPos}, {v} não encontrado")
elif vPos > pPos and pPos == -1:
    print(f"{v} encontrado em {vPos}, {p} não encontrado")
elif pPos < vPos and achou:
    print(f"{p} encontrado primeiro em {pPos}, {v} encontrado em {vPos}")
elif vPos < pPos and achou:
    print(f"{v} encontrado primeiro em {vPos}, {p} encontrado em {pPos}")
else:
    print(f"valores {p} e {v} não encontrados")

