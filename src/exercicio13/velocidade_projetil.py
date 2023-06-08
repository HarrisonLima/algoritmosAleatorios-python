def velocidade_projetil():
    distancia = float(input("Digite a distância percorrida em quilômetros: "))
    tempo = float(input("Digite o tempo gasto em minutos: "))

    velocidade = (distancia * 1000) / (tempo * 60)

    print(f"A velocidade do projétil é de {velocidade:.2f} metros por segundo.")

if __name__ == '__main__':
    velocidade_projetil()