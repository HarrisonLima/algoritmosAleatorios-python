def ajuste_salarial():
    salario = float(input("Digite o salário mensal: "))
    percentual = float(input("Digite o percentual de reajuste: "))

    novo_salario = salario + (salario * percentual / 100)

    print(f"O novo salário é: R$ {novo_salario:.2f}")

if __name__ == '__main__':
    ajuste_salarial()
