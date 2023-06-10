def fibonacci(numero):
    sequencia = [0, 1]

    while sequencia[-1] <= numero:
        proximo_termo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_termo)

    if sequencia[-1] > numero:
        sequencia.pop()

    return sequencia

numero = int(input("Digite um número: "))

sequencia = fibonacci(numero)

print("Sequência de Fibonacci até {}: {}".format(numero, sequencia))
