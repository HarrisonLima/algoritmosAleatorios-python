import math

def area_circunferencia():
    raio = float(input("Digite o valor do raio: "))
    area = math.pi * raio ** 2
    print("A área da circunferência é:", area)

if __name__ == '__main__':
    area_circunferencia()
