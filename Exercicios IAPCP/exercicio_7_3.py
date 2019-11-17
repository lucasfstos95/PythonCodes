#Exercicio 7.3 - manipulação string 3
s1 = "CTA"
s2 = "ABC"

array1 = list(s1)
array2 = list(s2)
aux_str = ""
for e in array2:
    if e not in s1:
      aux_str += e

for f in array1:
    if f not in s2:
      aux_str += f


print(f"Caracteres exclusivos: {aux_str}")