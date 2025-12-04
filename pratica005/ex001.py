#notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#print(notas.count(7))

#notas[-1] = 4

#print(max(notas))

#notas.sort()

#print(sum(notas) / len(notas))

#---------------------------------------------


palavras = ("Mario", "Luigi", "Peach", "Yoshi", "Browser")

for palavra in palavras:
    print(f"\nPalavra: {palavra.upper()}. Vogais: ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.upper(), end=" ")