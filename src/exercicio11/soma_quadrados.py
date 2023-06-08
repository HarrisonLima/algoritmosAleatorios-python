def soma_quadrados():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    resultado = valor1**2 + valor2**2 + valor3**2
    print(f'Resultado: {resultado}')

if __name__ == '__main__':
    soma_quadrados()