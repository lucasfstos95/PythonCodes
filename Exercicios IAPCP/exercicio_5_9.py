#Exercicio 5.9 - resto e divisão com contadores
n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite segundo numero: "))
aux1 = n1
r1=0
r2=0
while aux1>=n2:
    aux1 = aux1 - n2
    r1 = r1 + 1

while n1>=n2:
    n1 = n1 - n2

r2 = n1

print(f"Resultado inteiro de {n2}/{n2}: {r1}")
print(f"Resultado resto de {n2}/{n2}: {r2}")