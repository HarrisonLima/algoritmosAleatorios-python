def salario_liquido_professor():
    valor_hora_aula = float(input("Informe o número de horas trabalhadas no mês: "))
    horas_trabalhadas = float(input("Informe o valor da hora-aula: "))
    percentual_inss = float(input("Informe o percentual de desconto do INSS: "))

    salario_bruto = valor_hora_aula * horas_trabalhadas

    total_desconto = salario_bruto * (percentual_inss / 100)

    salario_liquido = salario_bruto - total_desconto

    print("Salário bruto: R$ %.2f" % salario_bruto)
    print("Salário líquido: R$ %.2f" % salario_liquido)


if __name__ == '__main__':
    salario_liquido_professor()