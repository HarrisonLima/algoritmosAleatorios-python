def letras_repetidas(texto):
    contador = {}

    for letra in texto:
        if letra.isalpha():
            if letra.lower() in contador:
                contador[letra.lower()] += 1
            else:
                contador[letra.lower()] = 1

    for letra in texto:
        if letra.isalpha() and contador[letra.lower()] == 1:
            return letra

    return None

texto = input("Digite um texto: ")

primeira_letra_nao_repetida = letras_repetidas(texto)

if primeira_letra_nao_repetida:
    print("A primeira letra não repetida é:", primeira_letra_nao_repetida)
else:
    print("Não existem letras que não se repetem no texto informado.")
