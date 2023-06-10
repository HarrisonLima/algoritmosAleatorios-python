def novo_jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate!"

    if jogador1 == "tesoura":
        if jogador2 == "papel" or jogador2 == "lagarto":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"

    if jogador1 == "papel":
        if jogador2 == "pedra" or jogador2 == "Spock":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"

    if jogador1 == "pedra":
        if jogador2 == "lagarto" or jogador2 == "tesoura":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"

    if jogador1 == "lagarto":
        if jogador2 == "Spock" or jogador2 == "papel":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"

    if jogador1 == "Spock":
        if jogador2 == "tesoura" or jogador2 == "pedra":
            return "Jogador 1 venceu!"
        else:
            return "Jogador 2 venceu!"

    return "Jogada inválida! Por favor, escolha entre tesoura, papel, pedra, lagarto ou Spock."

# Exemplo de uso:
jogador1 = input("Jogador 1, escolha sua jogada: ")
jogador2 = input("Jogador 2, escolha sua jogada: ")

resultado = novo_jokenpo(jogador1, jogador2)
print(resultado)
