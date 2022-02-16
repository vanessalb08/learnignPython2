def jogar():
    print("*" * 25, "\n   Jogo da Forca   \n", "*" * 25, sep="")

    palavra_secreta = "banana"
    letras_acertadas = ["_" for letra in palavra_secreta]  # cria a lista já um "_" para cada letra da palavra

    enforcou = False
    acertou = False
    erros = 0

    # enquanto ambos forem true
    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input("Fale uma letra")
        chute = chute.strip().lower()  # ignorar os espaços em branco e deixar tudo minusculo

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra  # adiciona a letra na posição do index
                index += 1
        else:
            erros += 1

        enforcou = erros == 6  # se errar 6x sai do laço
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if acertou:
            print("Você ganhou!")
        else:
            print("Você perdeu!")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
