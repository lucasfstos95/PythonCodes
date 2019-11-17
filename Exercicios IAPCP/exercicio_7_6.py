#Exercicio 7.6 - substituição de caracteres
s1 = "AATTGGAA"
s2 = "TG"
s3 = "AC"

s1 = list(s1)
s2 = list(s2)

for x, e in enumerate(s1):
    for y, f in enumerate(s2):
        if e == f:
            s1[x] = s3[y]
print(s1)
s1 = "".join(s1)
print(s1)

