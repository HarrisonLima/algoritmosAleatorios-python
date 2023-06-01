from email.policy import default

from src.exercicio11 import somaQuadrados
from src.exercicio12 import quadradoSoma
from src.exercicio13 import velocidadeProjetil

print("----------Listagem de exercícios----------")
print("A1. Two Fer (2-Fer)")
print("A2. Troca")
print("A3. Ajuste Salarial")
print("A4. FizzBuzz")
print("A5. Área de uma circunferência")
print("A6. Soma dos pares)")
print("A7. Salário Líquido Professor")
print("A8. Volume da caixa")
print("A9. Conversão em Real")
print("A10. Conversão em Dólar")
print("A11. Soma dos Quadrados")
print("A12. Quadrado da Soma")
print("A13. Velocidade do Projétil")
print("A14. Eleição Sindical")
print("A15. Média do Aluno")
print("A16. Somando Naturais")
print("A17. Ordenando Inteiros")
print("A18. Palíndromo")
print("A19. Scrabble Score")
print("A20. Fatorial")
print("A21. Algarismos Romanos")
print("A22. Primo")
print("A23. JoKenPo ")
print("A24. Pedra-papel-tesoura-lagarto-Spock")
print("A25. Soma dos pares")
print("A26. Anagramas")
print("A27. Letras repetidas")
print("A28. Fibonacci")
print("A29. Pangrama")
print("A30. Troco")
print("A31. Quebra de Linha")
print("A32. Sudoku")
print("----------------------------------------")


def switch_case(case):
    switch = {
        11: somaQuadrados.SomaQuadrados(),
        12: quadradoSoma.QuadradoSoma(),
        13: velocidadeProjetil.VelocidadeProjetil()
    }
    switch.get(case, default)()

if __name__ == '__main__':
    opcao = int(input("Digite o número do exercício que deseja executar: "))
    switch_case(opcao)
