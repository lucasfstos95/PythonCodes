#Exercicio 8.8 - minimo multiplo comum

def mdc(a, b):
    if b == 0:
        return a
    elif a > b:
        return mdc(b, (a%b))
    else:
        return None

def mmc(a, b):
    return abs(a*b)/mdc(a, b)

a = 15
b = 12
print(f"Resultado mmc({a}, {b}): {mmc(a, b)}")