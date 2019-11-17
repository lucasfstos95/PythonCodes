#Programa 6.13 - controle utilização sala de cinema
lugares_vagos = [10, 2, 1, 3, 0]

while True:
    print("\nDigite 0 para sair!")
    sala = int(input("Sala (1-5): "))
    if sala == 0:
        print("Fim do programa!")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida!")
    elif lugares_vagos[sala-1] == 0:
        print("Sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares deseja comprar ({lugares_vagos[sala-1]} disponíveis): "))
        if lugares > lugares_vagos[sala-1]:
            print("Quantidade disponível insuficiente!")
        elif lugares<0:
            print("Número invalido!")
        else:
            lugares_vagos[sala-1] -= lugares
            print(f"{lugares} lugares vendidos na sala {sala}")

    print("\n-= Utilização Das Salas =-")
    for i, e in enumerate(lugares_vagos):
        print(f"Sala[{i+1}]: {e} lugar(es) vazio(s)")

