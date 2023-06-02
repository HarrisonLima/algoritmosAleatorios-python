def ConversaoDolar():
    cotacao = float(input("Informe a cotação do dólar: "))
    valor_real = float(input("Informe a quantidade de reais disponível: "))

    valor_dolar = valor_real / cotacao

    print("O valor em dólar é: US$ {:.2f}".format(valor_dolar))
