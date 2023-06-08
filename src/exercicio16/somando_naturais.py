def somando_naturais():
    inicio = int(input("Insira o inicio do intervalo: "))
    fim = int(input("Insira o fim do intervalo: "))

    intervalo = fim - inicio

    if inicio > fim and intervalo <= 100:
        soma = sum(range(inicio, fim + 1))

        print(f"Intervalo: {inicio} a {fim}")
        print(f"Soma: {soma}")
    else:
        print(f"Intervalo: {inicio} a {fim} = {intervalo}")
        print(f"O intervalo deve ter no mínimo 100 números e o início do intervalo ser maior que o fim.")

if __name__ == '__main__':
    somando_naturais()