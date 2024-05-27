refazer = "s"
while refazer == "s":
    import random
    palavras = ["python", "java", "ruby", "javascript", "html", "css"]
    palavra = random.choice(palavras)
    letras_usuários = []
    tentativas = 5
    print("Bem-vindo ao Jogo da Forca!")
    while True:
        resultado = ""
        for letra in palavra:
            if letra in letras_usuários:
                resultado += letra
            else:
                resultado += "_"

        if resultado == palavra:
            print(resultado)
            print("Parabéns, você venceu! A palavra era: {}".format(palavra))
            break
        print(resultado)
        print("Tentativas restantes: {}".format(tentativas))
        letra = input("Digite uma letra: ").lower()
        if letra in letras_usuários:
            print("Você já usou esta letra.")
        elif letra in palavra:
            letras_usuários.append(letra)
        else:
            letras_usuários.append(letra)
            tentativas -= 1
        if tentativas == 0:
            print("Você perdeu! A palavra era: {}".format(palavra))
            break
        desenho = [
            "  +---+",
            "  |   |",
            "  O   |",
            " /|\\  |",
            " / \\  |",
            "      |",
        ]

        for i in range(5 - tentativas):
            print(desenho[i])
    print("Fim do Jogo da Forca!")
    refazer= input("Deseja continuar? [s/n] ").lower()
else:
    print("Programa encerrado.")
