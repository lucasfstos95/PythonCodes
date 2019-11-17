#exercicio 7.1 - Leitura string
s1 = "AABBEFAATT"
s2 = "BE"

if s2 in s1:
    p = s1.find(s2)
    print(f"'{s2}' encontrada na posição {p} de '{s1}'")
else:
    print("string não encontrada")