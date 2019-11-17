#Programa 6.22 - Exemplo de dicionario com estoque e operações de vendas
estoque = { "tomate":   [1000, 2.30],
            "alface":   [ 500, 0.45],
            "batata":   [2001, 1.20],
            "feijão":   [ 100, 1.50]    }

vendas = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas: \n")
for operacao in vendas:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo Total:  {total:21.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print(f"Descrição: {chave}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: R${dados[1]:6.2f}\n")
