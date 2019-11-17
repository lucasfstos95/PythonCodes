#Exercicio 6.13 - menor, maior e media
T = [-10, -8, 0, 1, 2, 5, -2, -4]

#Função retorna maior valor da lista
def maior(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max 

#Função retorna menor valor da lista
def menor(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min 

#Função retorna media da lista
def media(lista):
    x = 0
    soma = 0
    for i in lista:
        soma += i
        x += 1
    return (soma/x)

print(f"Temp máxima: {maior(T):.2f} °C")
print(f"Temp mínima: {menor(T):.2f} °C")
print(f"Temp média: {media(T):.2f} °C")