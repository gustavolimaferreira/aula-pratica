def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula a fatorial de um número inteiro.
    :param num:
    :return:
    """

    fat = 1
    if num == 0:
        return fat
    # esta parte só executa caso num > 0
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x= valida_int("Digite um valor para calular a fatorial: ", 0 , 99999)
print(f"{x}! = {fatorial(x)}")
