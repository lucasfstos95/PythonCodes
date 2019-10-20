#exercicio 5.22 - tabuada com opção de operação


#====== variaveis globais

op = 0
#======= Funções Operações ==========
def menu():
    print("Menu:")
    print("1 - adição")
    print("2 - subtração")
    print("3 - divisao")
    print("4 - multiplicação")
    print("5 - sair")
    

def som(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def div(a, b):
    return (a / b)

def mul(a, b):
    return (a * b)

def imprime(a, b, r, ope):
    print(f"{a} {ope} {b} = {r}")
#===================================#
menu()

while True:
    tabuada = 1
    numero = 1
    op = int(input("Escolha uma das opções acima e presione ENTER: "))
    if op==1:
        while tabuada<=10:
            imprime(tabuada, numero, tabuada+numero, '+')
            numero += 1
            if numero==11:
                numero = 1
                tabuada += 1
                print("\n===========================")
    elif op==2:
        while tabuada<=10:
            imprime(tabuada, numero, tabuada-numero, '-')
            numero += 1
            if numero==11:
                numero = 1
                tabuada += 1
                print("\n===========================")

    elif op==3:
        while tabuada<=10:
            imprime(tabuada, numero, tabuada/numero, '/')
            numero += 1
            if numero==11:
                numero = 1
                tabuada += 1
                print("\n===========================")

    elif op==4:
        while tabuada<=10:
            imprime(tabuada, numero, tabuada*numero, 'x')
            numero += 1
            if numero==11:
                numero = 1
                tabuada += 1
                print("\n===========================")

    elif op==5:
        print("Até a próxima!")
        break