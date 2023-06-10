def troco(total, pago):
    troco = pago - total

    cedulas = [100, 50, 10, 5, 1]
    moedas = [0.5, 0.1, 0.05, 0.01]

    troco_em_cedulas = []
    troco_em_moedas = []

    for cedula in cedulas:
        quantidade_cedulas = int(troco // cedula)
        if quantidade_cedulas > 0:
            troco_em_cedulas.append((cedula, quantidade_cedulas))
            troco -= quantidade_cedulas * cedula

    for moeda in moedas:
        quantidade_moedas = int(troco // moeda)
        if quantidade_moedas > 0:
            troco_em_moedas.append((moeda, quantidade_moedas))
            troco -= quantidade_moedas * moeda

    return troco_em_cedulas, troco_em_moedas

total = float(input("Digite o valor total a ser pago: "))
pago = float(input("Digite o valor efetivamente pago: "))

troco_em_cedulas, troco_em_moedas = troco(total, pago)

print("Troco em cédulas:")
for cedula, quantidade in troco_em_cedulas:
    print(f"{quantidade} cédula(s) de R${cedula}")

print("\nTroco em moedas:")
for moeda, quantidade in troco_em_moedas:
    print(f"{quantidade} moeda(s) de R${moeda:.2f}")
