def troca():
    # Leitura dos valores de A e B
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    # Troca dos valores
    A, B = B, A

    # Apresentação dos valores após a troca
    print("Valores após a troca:")
    print("A =", A)
    print("B =", B)

if __name__ == '__main__':
    troca()
