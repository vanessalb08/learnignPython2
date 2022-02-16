import forca
import adivinha

print("*" * 25, "\n   Escolha seu jogo   \n", "*" * 25, sep="")
print("(1) - Forca \n (2) - Adivinhação")

jogo = int(input("Qual jogo?"))
if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("jogando adivinhação")
    adivinha.jogar()
else:
    print("opção inválida")