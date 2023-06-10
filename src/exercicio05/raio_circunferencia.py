import math

def area_circunferencia(raio):
    pi = 3.14159265

    area = pi * raio ** 2

    return area

raio = float(input("Digite o valor do raio: "))

area_calculada = area_circunferencia(raio)

print("A área da circunferência é:", area_calculada)
