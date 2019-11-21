#Exercicio 8.6 - Como não escrever uma função

def soma(L):
    total = 0
    x = 0
    for x in L:
        total += x
    return total


L = [10, 20, 25, 30]
print(soma(L))
print(soma([10, 20, 25, 30, 1]))