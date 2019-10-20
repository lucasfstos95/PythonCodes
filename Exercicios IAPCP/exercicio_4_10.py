#exercicio 4.10 - conta de energia
kwh = int(input("Informe o KWh consumido: "))
print("Qual o seu tipo de instalação?")
print("R - Residência")
print("I - Indústria")
tipo = input("C - Comércio\n")

if tipo == 'R':
    if kwh>500:
        valor = kwh*0.65
    else:
        valor = kwh*0.4
elif tipo == 'I':
    if kwh>1000:
        valor = kwh*0.6
    else:
        valor = kwh*0.55
elif tipo == 'C':
    if kwh>5000:
        valor = kwh*0.6
    else:
        valor = kwh*0.55

print("Valor a pagar: R${:.2f}".format(valor))
