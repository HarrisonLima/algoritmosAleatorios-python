def soma_pares():
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))

    soma = 0
    for i in range(inicio, fim+1):
        if i % 2 == 0:
            soma += i

    print("A soma dos números pares no intervalo é:", soma)

if __name__ == '__main__':
    soma_pares()
