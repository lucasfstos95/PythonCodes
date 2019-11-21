#Programa 7.2 - Jogo da Forca
boneco = [['X','=','=',':','=','='],
          ['X',' ',' ',':',' ',' '],
          ['X',' ',' ',' ',' ',' '],
          ['X',' ',' ',' ',' ',' '],
          ['X',' ',' ',' ',' ',' '],
          ['X',' ',' ',' ',' ',' '],
          ['X','=','=','=','=','=']]
          
lista = ["abacaxi", "melancia", "morango", "abacate", "graviola", "pessego"]
numero = int(input("Digite um número para sorteio da palavra: "))
indice = (numero * 776)%len(lista)
palavra = lista[indice]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

for x in range(7):
        for y in range(6):
            print(boneco[x][y], end="")
        print()

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "-"
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você ja digitou essa letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    if erros == 1:
        boneco[2][3] = '0'
    elif erros == 2:
        boneco[3][3] = '|'
    elif erros == 3:
        boneco[3][2] = "\\"
    elif erros == 4:
        boneco[3][4] = '/'
    elif erros == 5:
        boneco[4][2] = '/'
    elif erros >= 6:
        boneco[4][4] = '\\'

    for x in range(7):
        for y in range(6):
            print(boneco[x][y], end="")
        print()
    
    if erros == 6:
        print("Enforcado!")
        print(f"Palavra: {palavra}")
        break
