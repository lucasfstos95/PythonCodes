#Exercício 5.4 - print numeros impares
lim = int(input("Digite o limite de impressão: "))
x = 1
while x<=lim:
    if x%2 != 0:
        print(f"{x} ,", end="")
    x += 1
