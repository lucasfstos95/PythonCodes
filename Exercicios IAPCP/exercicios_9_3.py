#Programa 9.3 - pares e impares
with open("arquivos/pares.txt", "r") as pares, open("arquivos/impares.txt", "r") as impares, open("arquivos/pareseimpares.txt", 'w') as pareseimpares:
    for par, impar in zip(pares.readlines(), impares.readlines()):
        pareseimpares.write(f'{par}{impar}')
          
    
with open("arquivos/pareseimpares.txt", 'r') as pareseimpares:
    print(pareseimpares.readlines())