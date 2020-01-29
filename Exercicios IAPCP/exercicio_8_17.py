#Exercício 8.17 - gerador de sequencia de fibonacci


def Fibonacci():
    prox = 1
    ant = 0
    while True:
        yield prox
        ant, prox = prox, prox + ant


gerador_fibonacci = (x for x in Fibonacci())


for e in gerador_fibonacci:
    print(e, end="")
    input()
