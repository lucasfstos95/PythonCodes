#Exercício 4.8 - operações
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
print("Qual operação deseja realizar?")
op = int(input("1-soma | 2-subt. | 3-mult. | 4-div. : "))

if op==1:
    r = n1+n2
    print(f"O resultado da operação {n1:.2f} + {n2:.2f} = {r:.2f} ")
elif op==2:
    r = n1-n2
    print(f"O resultado da operação {n1:.2f} - {n2:.2f} = {r:.2f} ")
elif op==3:
    r = n1*n2
    print(f"O resultado da operação {n1:.2f} * {n2:.2f} = {r:.2f} ")
elif op==4:  
    r = n1/n2
    print(f"O resultado da operação {n1:.2f} / {n2:.2f} = {r:.2f} ")

