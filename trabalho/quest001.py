print("Bem vindo ao sistema de Gustavo Ferreira")

valorBase = float(input("Informe o valor base Plano: "))
idade = int(input("Informe a idade do cliente: "))
#estrutura condicional para definir a porcentagem conforme a idade
if idade >= 0 and idade < 19:
    porcentagem = 100/100
elif idade >= 19 and idade < 29:
    porcentagem = 150/100
elif idade >= 29 and idade < 39:
    porcentagem = 225/100
elif idade >= 39 and idade < 49:
    porcentagem = 350/100
elif idade >= 49 and idade < 59:
    porcentagem = 600/100
else:
    porcentagem = 0
    print("Idade inválida")

valorMensal = valorBase * porcentagem

print(f"O valor mensal do plano é: R${valorMensal:.2f}")