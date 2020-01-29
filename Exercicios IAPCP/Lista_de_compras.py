"""
    SCRIPT: LISTA DE COMPRAS VIRTUAL
    AUTOR: LUCAS FELIPE
    DATA: NOV/2019
"""

ESPACAMENTO = 20
lista_compra = {}       #DICIONÁRIO DE PRODUTOS

def ImprimeLinha(item, quantidade, valor):
    print("{:3d} x {:-<35s} R${: >6.2f}  ".format(quantidade, item + " ", valor))

def EncerrarCompra():
    s = input("Deseja add mais produtos? (s/n)")
    if s == 's':
        return False
    else:
        TotalCompra()
        return True

def TotalCompra():
    global lista_compra
    global ESPACAMENTO
    total = 0
    for item, parametros in lista_compra.items():
        preco, quantidade = parametros
        total += preco*quantidade
        ImprimeLinha(item, quantidade, preco*quantidade)
    print("="*50)
    print("TOTAL:{:-<35s} R${:6.2f}".format(" ",total))

def AddLista(dic):
    global lista_compra
    item = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preco do produto: "))
    lista_compra[item] = [preco, quantidade]
    valor_parcial = quantidade * preco
    print("Adicionado: ", end="")
    ImprimeLinha(item, quantidade, valor_parcial)
    

while True:
    print(lista_compra)
    AddLista(lista_compra)
    if EncerrarCompra():
        break