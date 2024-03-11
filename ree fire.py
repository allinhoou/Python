print("**************")
print("Bem-Viendo no jogo adivinhação")
print("**************")

numer_secreto = 46
chute_sorte = input("Digite o seu numero")
print("Você digitou", chute_sorte)
chute = int(chute_sorte)


acertou = chute == numer_secreto
maior = chute > numer_secreto
menor = chute < numer_secreto
if(acertou):
    print("Você acertou!!")
else:
    if(maior):
        print("Você errou!! o seu chute foi maior que o numero secreto")

    elif(menor):
        print("Você errou!! o seu chute foi menor que o numero secreto")
        print("Fim de jogo")