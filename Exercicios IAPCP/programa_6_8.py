#Programa 6.8 - Pilha de pratos
ultimo = 5
pilha = list(range(1, ultimo+1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E, D ou S):")
    if operacao == "D":
        if len(pilha)>0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia, nada para lavar.")
    elif operacao == "E":
        ultimo += 1  #novo prato
        pilha.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida, Digite apenas E, D ou S.")
