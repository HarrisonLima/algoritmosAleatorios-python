def palindromo():
    entrada = input("Digite uma palavra, frase ou número: ")
    entrada = entrada.lower()

    if entrada == entrada[::-1]:
        print(f"{entrada} é um palíndromo.")
    else:
        print(f"{entrada} não é um palíndromo.")

if __name__ == '__main__':
    palindromo()