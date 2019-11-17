#Exercicio 7.5 - excluir chars de uma string da outra
s1 = "AATTGGAA"
s2 = "TG"
s1 = list(s1)
s2 = list(s2)
for e in s2:
    tam = len(s1)-1
    x=0
    while x <= tam:
        if e == s1[x]:
            del s1[x]
            tam = len(s1)-1
        else:
            x += 1    
        print(s1)
