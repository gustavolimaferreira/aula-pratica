print(10 * "-", "Bem vindo a Pizzária do Gustavo Ferreira", 10 * "-", "\n", 25 * "-", "Cardápio", 25 * "-", "\n", 60 * "-", "\n", 3 * "-", "|  Tamanho  | Pizza Salgada(PS) |  Pizza Doce(PD)  |", 3 * "-", "\n", 3 * "-", "|     P     |       R$30,00     |      R$34,00     |", 3 * "-", "\n", 3 * "-", "|     M     |       R$45,00     |      R$48,00     |", 3 * "-", "\n", 3 * "-", "|     G     |       R$60,00     |      R$66,00     |", 3 * "-", "\n", 60 * "-")

totalPedido = 0

def calcularValor(sabor, tamanho):
    if sabor == "PS":
        if tamanho == "P":
            return 30
        elif tamanho == "M":
            return 45
        elif tamanho == "G":
            return 60
    elif sabor == "PD":
        if tamanho == "P":
            return 34
        elif tamanho == "M":
            return 48
        elif tamanho == "G":
            return 66

while True:

    while True:
        sabor = input("Entre com o sabor desejado (PS/PD): ").upper()
        if sabor == "PS" or sabor == "PD":
            break
        else:
            print("Sabor inválido. Tente novamente\n")

    while True:
        tamanho = input("Entre com o tamnanho desejado (P/M/G): ").upper()
        if tamanho in ["P", "M", "G"]:
            break
        else:
            print("Tamanho inválido. Tente novamente\n")

    valorPizza = calcularValor(sabor, tamanho)
    totalPedido += valorPizza

    print(f"Você pediu uma Pizza {sabor} no tamanho {tamanho}: R${valorPizza:.2f}")

    continuar = input("\nDeseja mais alguma coisa? (S/N): ").upper()

    if continuar != "S":
        break

print(f"\nO valor total a ser pago: R${totalPedido:.2f}\n")