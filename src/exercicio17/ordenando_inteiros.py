def ordenando_inteiros():
    array = []
    for i in range(12):
        elemento = int(input(f"Digite o elemento {i + 1}: "))
        array.append(elemento)

    array_ordenado = sorted(array, reverse=True)

    print("Elementos ordenados em ordem decrescente:")
    for elemento in array_ordenado:
        print(elemento)

