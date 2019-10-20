
valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50.0
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas += 1
    else:
        if atual>=1.0 and cedulas!=0:
            print(f"{cedulas} cédula(s) de R${atual}")
        elif atual<1.0 and cedulas!=0: 
            print(f"{cedulas} moeda(s) de R${atual}")
        
        
        if apagar==0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        else:
            break
        cedulas = 0