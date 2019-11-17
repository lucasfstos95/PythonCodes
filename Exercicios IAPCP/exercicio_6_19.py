#Exercicio 6.19 - Conjuntos 1

def getRepete(A):
    L = list(A)                     # lista auxiliar
    L.sort()                        # ordena a lista
    conj = set(list(L))             # gerando conjunto dessa lista
    conj = list(conj)               # convertendo o conjunto em lista
    conj.sort()                     # ordenação da segunda lista
    tam = len(conj)                 # tamanho da segunda lista 
    x = 0                           # indexador primeira lista    
    while tam > 0:                  # enquanto a lista a ser comparada não tiver tamanho zero
        if conj[0] == L[x]:         # apaga ambos os numeros caso forem iguais
            del conj[0]
            del L[x]
        else: 
            x += 1                  # incrementa indexador da lista dos repetidos, pois foi encontrado um repetido
        tam = len(conj)             # recalcula o tamanho da lista encontrada
    return L                        # retorna a lista com os valores repetidos


A = [1, 3, 4, 4, 5, 6, 7, 7]
B = [1, 2, 2, 5, 6, 7, 8, 9]

a = set(list(A))
b = set(list(B)) 

print(f"\nComuns: {a|b}")
print(f"somente em A: {a-b}")
print(f"somente em B: {b-a}")

c = set(A+B)                      #concatene as duas listas e converte em conjunto
d = getRepete(A) + getRepete(B)   #concatena as duas listas com os elementos que repetem em cada uma
d = set(d)                        #converte em um conjunto
print(f"união não repetem: {c-d}")

e = set(getRepete(B))
print(f"Primeira sem os repetidos na segunda: {a-e}\n")


