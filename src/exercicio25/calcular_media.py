def calcular_media(numeros):
    if len(numeros) == 0:
        return 0

    soma = sum(numeros)
    media = soma / len(numeros)
    return media


numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")

    if entrada.lower() == "sair":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

media = calcular_media(numeros)
print("A média dos números informados é:", media)
