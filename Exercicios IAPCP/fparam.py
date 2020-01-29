#Exercício 9.1- Manipulando arquivos pelo terminal
import sys
print(f"Numero de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")