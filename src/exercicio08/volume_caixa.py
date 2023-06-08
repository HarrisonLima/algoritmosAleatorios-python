def volume_caixa():
    comprimento = float(input("Digite o comprimento da caixa: "))
    largura = float(input("Digite a largura da caixa: "))
    altura = float(input("Digite a altura da caixa: "))

    volume = comprimento * largura * altura

    print("O volume da caixa é:", volume)

if __name__ == '__main__':
    volume_caixa()