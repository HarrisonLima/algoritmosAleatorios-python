def conversao_real():
    cotacao = float(input("Digite a cotação do dólar: "))
    dolares = float(input("Digite a quantidade de dólares disponível: "))
    conversao = cotacao * dolares
    print("O valor em reais (R$) é: %.2f" % conversao)

if __name__ == '__main__':
    conversao_real()