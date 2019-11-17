#Programa 6.17 - Exemplo de dicionario com estoque e operações de vendas
estoque = { "tomate":   [1000, 2.30],
            "alface":   [ 500, 0.45],
            "batata":   [2001, 1.20],
            "feijao":   [ 100, 1.50]    }
vendas = []
total = 0
print("Vendas: ")
while True:
    op = input("\nAdd produto? (s/n): ")
    if op == 'n':
        print("\nTotal de compras:")
        break
    
    produto = input("Digite o produto desejado: ")
    quantidade = int(input("Digite a quantidade desejada: "))
    parcial = [produto, quantidade]    
    if produto in estoque:
        estoque[produto][0] -= quantidade
        vendas.append(parcial)
        print(f"vendas = {vendas})
    else: 
        print("produto não encontrado!")

for operacao in vendas:
        produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
        total += custo

print(f"Custo Total:  {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print(f"Descrição: {chave}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: R${dados[1]:6.2f}\n")
