#Programa 8.7 - Função recursiva de fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Digite um número inteiro: "))
print(f"Resultado fibonacci({n}): {fibonacci(n)}")