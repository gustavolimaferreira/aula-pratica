A = int(input("Digite o 1o lado do triângulo: "))
B = int(input("Digite o 2o lado do triângulo: "))
C = int(input("Digite o 3o lado do triângulo: "))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
    #Se chegou até aqui o triângulo é valido!
    if (A != B and A != C and B != C):
        print("Triângulo escaleno!")
    else:
        if (A == B and B == C):
            print("Triângulo equilátero!")
        else:
            print("Triângulo isósceles!")
else:
    print("Ao menos um dos valores indicados não servem para formnar um triângulo.")