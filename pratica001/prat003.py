# 2. Escreva um programa que pergunte a quantidade de km percorridos por um ccarro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o ccarro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input("Quantos Km foram percorridos? "))
dias = int(input("Quantos dias foram percorridos? "))

preco = 60 * dias + 0.15 * km
print(f"Km = {km}. Dias: {dias}.")
print(f"Valor a ser pago: {preco}")