#Exercício 8.10 - Fibonacci sem recursividade

def fibonacci(n):
    last = 0
    atual = 1
    while n > 1:
        aux = atual
        atual = atual + last
        last = aux
        n -= 1
    return atual

n = int(input("Digite um número inteiro: "))
print(f"Resultado fibonacci({n}): {fibonacci(n)}")