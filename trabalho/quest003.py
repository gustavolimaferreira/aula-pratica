print("Bem vindo a Madeireira do Lenhador Gustavo Ferreira")

total = 0
#funções do programa
def escolha_tipo():#função para escolher o tipo de madeira
    while True:
        madeira = input("\nEntre com o Tipo de Madeira desejado\n PIN - Tora de Pinho\n PER - Tora de Peroba\n MOG - Tora de Mogno\n IPE - Tora de Ipê\n IMB - Tora de Imbuia\n ")
               
        if madeira == "PIN":
            return "PIN", 150.40
        elif madeira == "PER":
            return "PER", 170.20
        elif madeira == "MOG":
            return "MOG", 190.90
        elif madeira == "IPE":
            return "IPE", 210.10
        elif madeira == "IMB":
            return "IMB", 220.70
        else:
            print("Escolha inválida, entre com o modelo novamente")


def qtd_toras():#função para escolher a quantidade de toras
    try:
        while True:
            qtdToras = int(input("Entre com a quantidade de toras (m³): "))
            if qtdToras <= 2000 and qtdToras >= 0:
                if qtdToras < 100:
                    desconto = 0
                elif 100 <= qtdToras < 500:
                    desconto = 0.04
                elif 500 <= qtdToras < 1000:
                    desconto = 0.09
                elif 1000 <= qtdToras <=2000:
                    desconto = 0.16
                
                return qtdToras, desconto
            else:
                print("Não aceitamos pedidos com essa quantidade de toras.\nPor favor entre com a quantidade novamente.")
    except ValueError:
        print("Valor invalido! Por favor, insira um numero valido para a quantidade.")

def transporte():#função para escolher o tipo de transporte
    while True:
        tipoTransporte = input("Escolha o tipo de Transporte:\n1 - Transporte Rodoviário - R$ 1000.00\n2 - Transporte Ferroviario - R$ 2000.00\n3 - Transporte Hidroviário - R$2500.00\n")

        if tipoTransporte == "1":
            return "Rodoviario", 1000
        elif tipoTransporte == "2":
            return "Ferroviario", 2000
        elif tipoTransporte == "3":
            return "Hidroviario", 2500
        else:
            print("Opção invalida! Por favor, digite uma das opções válidas (1, 2 ou 3).")
#programa principal
tipoMadeira, valorMadeira = escolha_tipo()
qtdToras, desconto = qtd_toras()
tipoTransporte, valorTransporte = transporte()

total = ((valorMadeira * qtdToras) * (1 - desconto)) + valorTransporte#calculo do valor total

print(f"\nPedido realizado com sucesso!")
print(f"Tipo de madeira: {tipoMadeira}\nQuantidade de Toras (m³): {qtdToras}m³\nTransporte escolhido: {tipoTransporte}\nValor total a pagar: R${total:.2f}")