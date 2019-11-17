#Programa 6.20 - Bubble Sort
L = [3, 3, 1, 5, 4]

fim = len(L)
while fim > 1:   
    trocou = False
    x = 0
    while x < (fim-1):
        if L[x] > L[x+1]:
            trocou = True
            aux = L[x]
            L[x] = L[x+1]
            L[x+1] = aux
        x +=1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(f"{e}-", end="")
print()