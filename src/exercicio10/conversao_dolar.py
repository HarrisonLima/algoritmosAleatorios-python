def conversao_dolar():
    cotacao = float(input("Informe a cotação do dólar: "))
    valor_real = float(input("Informe a quantidade de reais disponível: "))

    valor_dolar = valor_real / cotacao

    print("O valor em dólar é: US$ {:.2f}".format(valor_dolar))

if __name__ == '__main__':
    conversao_dolar()