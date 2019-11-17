#Exercicio 6.5 - fila
ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"File atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    op = input("Operação (F, A ou S):")
    i = 0
    for i in range(len(op)):
        operacao = op[i]
        if operacao == "A":
            if len(fila)>0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia, ninguem para atender.")
        elif operacao == "F":
            ultimo += 1  #incrementa o ticket do novo cliente
            fila.append(ultimo)
            print(f"Cliente {ultimo} adicionado a fila")
        elif operacao == "S":
            print("Fim operação!")
            break
        else:
            print("Operação inválida, Digite apenas F, A ou S.")
        i += 1

