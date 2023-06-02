def ConversaoReal():
    cotacao = float(input("Digite a cotação do dólar: "))
    dolares = float(input("Digite a quantidade de dólares disponível: "))
    conversao = cotacao * dolares
    print("O valor em reais (R$) é: %.2f" % conversao)
