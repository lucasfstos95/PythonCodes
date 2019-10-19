#Exercício 4.9 - aprovação de empréstimo
valor = float(input("Qual o valor da casa a comprar? "))
salario = float(input("Qual o seu salario atual? "))
periodo = int(input("Deseja pagar em qtos anos? "))

meses = 12*periodo
salario_30 = salario*0.3
prestacao = valor/meses

if prestacao>salario_30:
    print("Seu empréstimo não foi aprovado, salário não compatível com o período de pagamento!")
else:
    print("Empréstimo aprovado!")
