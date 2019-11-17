#Exercicio 7.2 - manipulação strings 2
s1 = "AAACTBF"
s2 = "CBT"

array = list(s2)
aux_str = ""
for e in array:
    if e in s1:
      aux_str += e

print(f"Caracteres em comum: {aux_str}")