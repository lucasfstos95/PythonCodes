#Exercicio 6.2 - fila dupla
ultimo_1 = 10
ultimo_2 = 10
fila1 = list(range(1, ultimo_1+1))
fila2 = list(range(1, ultimo_2+1))

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1")
    print(f"Fila 1 atual: {fila1}")
    print(f"Existem {len(fila2)} clientes na fila 2")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    op = input("Operação (F, A ou S):")
    
    i = 0
    for i in range(len(op)):
        operacao = op[i]
        if operacao == "A":
            if len(fila1)>0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido fila 1")
            else:
                print("Fila 1 vazia, ninguem para atender.")
        elif operacao == "B":
            if len(fila2)>0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido fila 2")
            else:
                print("Fila 2 vazia, ninguem para atender.")
        elif operacao == "F":
            ultimo_1 += 1  #incrementa o ticket do novo cliente
            fila1.append(ultimo_1)
            print(f"Cliente {ultimo_1} adicionado a fila 1")
        elif operacao == "G":
            ultimo_2 += 1  #incrementa o ticket do novo cliente
            fila2.append(ultimo_2)
            print(f"Cliente {ultimo_2} adicionado a fila 2")
        elif operacao == "S":
            print("Fim operação!")
            break
        else:
            print("Operação inválida, Digite apenas F, A ou S.")
        i += 1

