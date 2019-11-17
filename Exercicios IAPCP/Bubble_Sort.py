L = [7, 4, 5, 3, 15, 16, 8, 1, 20]

"""
    FUNÇÃO: Bubble Sort
    PARAM:  L(lista)
"""
def BubbleSort(L):
    fim = len(L)
    while fim > 1:
        trocou = False
        x = 0
        for x in range(fim-1):
            if L[x] > L[x+1]:
                trocou = True
                aux = L[x]
                L[x] = L[x+1]
                L[x+1] = aux
        if not trocou:
            break
        fim -= 1
    return L    
 # Fim BubbleSort   


## main
for e in BubbleSort(L):
    print(e)
            
        

