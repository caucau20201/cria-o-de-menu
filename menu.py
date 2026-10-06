#menu com py
while True:
    print("                       ")
    print("    🎮Play Games🎮     ")
    print("                       ")

#modos de jogo
    print(" 1 - 🔮 Jogo de Adivinhação 🔮")
    print(" 2 - ➋ Jogo do Par ou Ímpar ❶")
    print(" 3 - 🎲 Dado 🎲")
    print(" 0 - ❌ Sair ❌")

#captura a opção do usuário como um número iteiro
    opcao = int(input(" Escolha uma opção: "))

#verificar o que o usuário escolheu
    if opcao == 1:
        print("Você escolheu o 🔮 Jogo de Adivinhação 🔮")
    elif opcao == 2: 
        print("Você escolheu o ➋ Jogo do Par ou Ímpar ❶")
    elif opcao == 3:
        print("Você escolheu o 🎲 Dado 🎲")
    elif opcao == 0:
        print("Até logo")
        break # interronpe o loop while e fechar o programa
    else:
        print("Digite uma opção valida")
