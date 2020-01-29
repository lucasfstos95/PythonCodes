#Exercicio 8.16 - gerador numeros primos


def IsPrimo(x):
    for i in range(x-1, 1, -1):
        if x%i == 0:
            return False
    return True


gerador_primos = (x for x in range(1, 50) if (IsPrimo(x) and x != 1))


for x in gerador_primos:
    print(x)
