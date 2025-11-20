#i = 3
#while (i < 13):
#    print(i)
#    i += 1

#for i in range(3, 13, 1):
#    print(i)

#for i in range(0, 9, 2):
#    print(i)

#i = 0
#while (i <= 8):
#    print(i)
#    i += 2

#01.

print("LANCHONETE")
print("1 - Coxinha R$ 5,00")
print("2 - Pastel R$ 7,00")
print("3 - Café R$ 4,00")
print("4 - Suco R$ 6,00")
print("5 - SAIR")

total = 0
while True:
    op = int(input("Qual item gostaria de comprar? "))
    

    if (op == 1):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 5.00
    elif (op == 2):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 7.00
    elif (op == 3):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 4.00
    elif (op == 4):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 6.00
    elif (op == 5):
        break
    else:
        print("Produto inválido. Selecione outro.")
    
print(f"O total a ser gasto nesse pedido é de R$ {total}.")