def quebra_linhas(frase, colunas):
    palavras = frase.split()
    linhas = []
    linha_atual = ''

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= colunas:
            if linha_atual != '':
                linha_atual += ' '
            linha_atual += palavra
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    linhas.append(linha_atual)

    return linhas


frase = input("Digite a frase: ")
colunas = int(input("Digite a quantidade de colunas: "))

linhas_quebradas = quebra_linhas(frase, colunas)

for linha in linhas_quebradas:
    print(linha)
