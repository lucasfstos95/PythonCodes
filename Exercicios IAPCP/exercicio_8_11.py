#Exercicio 8.11 - validação de string

def TamanhoString(s, min, max):
    s_size = len(s)
    if min <= s_size <= max:
        return True
    else:
        return False
String = "Lucas Felipe" #tam = 12
print(TamanhoString(String, 5, 15))