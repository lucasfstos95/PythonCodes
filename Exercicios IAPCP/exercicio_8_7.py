#Exercicio 8.7 - maximo divisor comum

def mdc(a, b):
    if b == 0:
        return a
    elif a > b:
        return mdc(b, (a%b))
    else:
        return None

a = 15
b = 12
print(f"Resultado mdc({a}, {b}): {mdc(a, b)}")