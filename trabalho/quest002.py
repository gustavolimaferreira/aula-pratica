print(10 * "-", "Bem vindo a Pizzária do Gustavo Ferreira", 10 * "-", "\n", 25 * "-", "Cardápio", 25 * "-", "\n", 60 * "-", "\n", 3 * "-", "|  Tamanho  | Pizza Salgada(PS) |  Pizza Doce(PD)  |", 3 * "-", "\n", 3 * "-", "|     P     |       R$30,00     |      R$34,00     |", 3 * "-", "\n", 3 * "-", "|     M     |       R$45,00     |      R$48,00     |", 3 * "-", "\n", 3 * "-", "|     G     |       R$60,00     |      R$66,00     |", 3 * "-", "\n", 60 * "-")

totalPedido = 0
#Funções do programa
def calcularValor(sabor, tamanho):#função para saber o valor de cada pizza
    if sabor == "PS":#pizza salgada
        if tamanho == "P":
            return 30
        elif tamanho == "M":
            return 45
        elif tamanho == "G":
            return 60
    elif sabor == "PD":#pizza doce
        if tamanho == "P":
            return 34
        elif tamanho == "M":
            return 48
        elif tamanho == "G":
            return 66

while True:#loop principal do programa

    while True:#loop do sabor
        sabor = input("Entre com o sabor desejado (PS/PD): ").upper()
        if sabor == "PS" or sabor == "PD":
            break
        else:
            print("Sabor inválido. Tente novamente\n")

    while True:#loop do tamanho
        tamanho = input("Entre com o tamnanho desejado (P/M/G): ").upper()
        if tamanho in ["P", "M", "G"]:
            break
        else:
            print("Tamanho inválido. Tente novamente\n")

    valorPizza = calcularValor(sabor, tamanho)#calculo do valor da pizza
    totalPedido += valorPizza

    print(f"Você pediu uma Pizza {sabor} no tamanho {tamanho}: R${valorPizza:.2f}")

    continuar = input("\nDeseja mais alguma coisa? (S/N): ").upper()

    if continuar != "S":#para parar o pedido
        break

print(f"\nO valor total a ser pago: R${totalPedido:.2f}\n")