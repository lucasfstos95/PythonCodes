#Exercicio 7.4 - contador de caracteres
s = "TTAAC"
dic = {}
for e in s:
    if e not in dic:
        dic[e] = 1
    else:
        dic[e] += 1

for chave, valor in dic.items():
    print(f"char {chave}: {valor}x")
   