#Exercicio 7.10 - Jogo da velha

#Variaveis globais
simbolo = ['0', 'X']
#          00   01   02     10   11    12    20   21   22
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogador = 0 
op = 0 

#Função retorna se a matriz está cheia ou não
def matrizCheia(matriz):
    for x in range(3):
        for y in range(3):
            if matriz[x][y] == ' ':
                return False
    return True

#FUNÇÃO VERIFICA SE ALGUEM VENCEU O JOGO
def checkVencedor(matriz):
    global jogador                                              #DECLARANDO USO DA VARIAVEL GLOBAL
    linhas = ""                                                 #STRING LOCAIS
    diagonal1 = ""  # 00, 11, 22                                
    diagonal2 = ""  # 20, 11, 02
    for i in range(3):
        linha = "".join(matriz[i])                              #ATRIBUI A STRING A LINHA DA MATRIZ

        diagonal1 += "".join(matriz[i][i])                      #CONCATENA CARACTERES DA DIAGONAL PRINCIPAL
        #-2x-2y+4=0
        k = (4-2*i)//2
        diagonal2 += "".join(matriz[k][i])
        coluna = ""
        for j in range(3):
            coluna += "".join(matriz[j][i])
                                                                #CHECK SE ALGUMA LINHA FOI PREENCHIDA POR ALGUM JOGADOR                 
        if linha == "000" or coluna == "000" or diagonal1 == "000" or diagonal2 == "000":
            return 1
        if linha == "XXX" or coluna == "XXX" or diagonal1 == "XXX" or diagonal2 == "XXX":
            return 2
    else:
        if matrizCheia(matriz):                                 #MATRIZ CHEIA MAS NINGUEM GANHOU
             return 3
        else:                                                   #MATRIZ INCOMPLETA MAS AINDA SEM VENCEDOR
            return -1
#ALTERNA ENTRE OS JOGADORES
def alternaJogador():
    global jogador                                              #VARIAVEL GLOBAL DO SCRIPT
    jogador = 2 if jogador == 1 else 1                          #inverte o jogador da rodada

#COLOCA CARACTER NO LOCAL DEVIDO DA MATRIZ
def putChar(x, y, z):                                           
    pulaLinha()
    if not(matriz[x][y] == ' '):                                #POSIÇÃO JA PREENCHIDA
        print("Jogada inválida, escolha outra posição!")
    else:
        matriz[x][y] = z                                        #ATRIBUIÇÃO CARACTERE A MATRIZ
        alternaJogador()

#PULA ALGUMAS LINHAS NO TERMINAL 
def pulaLinha():
    esp = "\n"*100                                                         
    print(esp)

#IMPRIME O TABULEIRO ATUALIZADO NA TELA
def printTabuleiro(tabuleiro):                                              
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")
    print(f"---+---+---")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
    print(f"---+---+---")
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
    
alternaJogador()
#main loop
while True:  
    #VERIFICA OPÇÃO ESCOLHIDA PELO JOGADOR
    if op == 1:
        putChar(0, 0, simbolo[jogador-1])
    elif op == 2:
        putChar(0, 1, simbolo[jogador-1])
    elif op == 3:
        putChar(0, 2, simbolo[jogador-1])
    elif op == 4:
        putChar(1, 0, simbolo[jogador-1])
    elif op == 5:
        putChar(1, 1, simbolo[jogador-1])
    elif op == 6:
        putChar(1, 2, simbolo[jogador-1])
    elif op == 7:
        putChar(2, 0, simbolo[jogador-1])
    elif op == 8:
        putChar(2, 1, simbolo[jogador-1])
    elif op == 9:
        putChar(2, 2, simbolo[jogador-1])

    printTabuleiro(matriz)
    #CHECK SE OUVE VENCEDOR
    if checkVencedor(matriz) == 1:
        print("Fim de jogo...\nJogador 1 venceu!")
        break
    elif checkVencedor(matriz) == 2:
        print("Fim de jogo...\nJogador 2 venceu!")
        break
    elif checkVencedor(matriz) == 3:
        print("Fim de jogo...\nEmpate!")
        break
    else:
        print(f"\nJogador {jogador}")
        op = int(input("Digite a posição que deseja jogar: "))
#end main loop