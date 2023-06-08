def eleicao_sindical():
    votos_candidato_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
    votos_candidato_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
    votos_candidato_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))

    votos_nulos = int(input("Digite a quantidade de votos nulos: "))
    votos_branco = int(input("Digite a quantidade de votos em branco: "))

    total_eleitores = votos_candidato_a + votos_candidato_b + votos_candidato_c + votos_nulos + votos_branco

    print("---- Resultados ----")
    print("Total de eleitores:", total_eleitores)
    print("Percentual de votos válidos em relação à quantidade de eleitores:", ((votos_candidato_a + votos_candidato_b + votos_candidato_c) / total_eleitores), "%")
    print("Percentual de votos válidos do candidato A em relação à quantidade de eleitores:", (votos_candidato_a / total_eleitores), "%")
    print("Percentual de votos válidos do candidato B em relação à quantidade de eleitores:", (votos_candidato_b / total_eleitores), "%")
    print("Percentual de votos válidos do candidato C em relação à quantidade de eleitores:", (votos_candidato_c / total_eleitores), "%")
    print("Percentual de votos nulos em relação à quantidade de eleitores:", (votos_nulos / total_eleitores), "%")
    print("Percentual de votos em branco em relação à quantidade de eleitores:", (votos_branco / total_eleitores), "%")

if __name__ == '__main__':
    eleicao_sindical()