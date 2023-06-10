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

exercise = int(input("Digite o número do exercício que deseja executar: "))
if exercise == 1:
    from src.exercicio01 import two_fer
    two_fer.two_fer()
elif exercise == 2:
    from src.exercicio02 import troca
    troca.troca()
elif exercise == 3:
    from src.exercicio03 import ajuste_salarial
    ajuste_salarial.ajuste_salarial()
elif exercise == 4:
    from src.exercicio04 import fizz_buzz
    fizz_buzz.fizz_buzz()
elif exercise == 5:
    from src.exercicio05 import raio_circunferencia
    raio_circunferencia.area_circunferencia()
elif exercise == 6:
    from src.exercicio06 import soma_pares
    soma_pares.soma_pares()
elif exercise == 7:
    from src.exercicio07 import salario_liquido_professor
    salario_liquido_professor.salario_liquido_professor()
elif exercise == 8:
    from src.exercicio08 import volume_caixa
    volume_caixa.volume_caixa()
elif exercise == 9:
    from src.exercicio09 import conversao_real
    conversao_real.conversao_real()
elif exercise == 10:
    from src.exercicio10 import conversao_dolar
    conversao_dolar.conversao_dolar()
elif exercise == 11:
    from src.exercicio11 import soma_quadrados
    soma_quadrados.soma_quadrados()
elif exercise == 12:
    from src.exercicio12 import quadrado_soma
    quadrado_soma.quadrado_soma()
elif exercise == 13:
    from src.exercicio13 import velocidade_projetil
    velocidade_projetil.velocidade_projetil()
elif exercise == 14:
    from src.exercicio14 import eleicao_sindical
    eleicao_sindical.eleicao_sindical()
elif exercise == 15:
    from src.exercicio15 import media_aluno
    media_aluno.media_aluno()
elif exercise == 16:
    from src.exercicio16 import somando_naturais
    somando_naturais.somando_naturais()
elif exercise == 17:
    from src.exercicio17 import ordenando_inteiros
    ordenando_inteiros.ordenando_inteiros()
elif exercise == 18:
    from src.exercicio18 import palindromo
    palindromo.palindromo()
elif exercise == 19:
    from src.exercicio19 import scrabble_score
    scrabble_score.scrabble_score()
elif exercise == 20:
    from src.exercicio20 import fatorial
    fatorial.fatorial()
elif exercise == 21:
    from src.exercicio21 import algarismos_romanos
    algarismos_romanos.algarismos_romanos()
elif exercise == 22:
    from src.exercicio22 import primo
    primo.primo()
elif exercise == 23:
    from src.exercicio23 import jokenpo
    jokenpo.jokenpo()
elif exercise == 24:
    from src.exercicio24 import novo_jokenpo
    novo_jokenpo.novo_jokenpo()
elif exercise == 25:
    from src.exercicio25 import calcular_media
    calcular_media.calcular_media()
elif exercise == 26:
    from src.exercicio26 import anagrama
    anagrama.anagrama()
elif exercise == 27:
    from src.exercicio27 import letras_repetidas
    letras_repetidas.letras_repetidas()
elif exercise == 28:
    from src.exercicio28 import fibonacci
    fibonacci.fibonacci()
elif exercise == 29:
    from src.exercicio29 import pangrama
    pangrama.pangrama()
elif exercise == 30:
    from src.exercicio30 import troco
    troco.troco()
elif exercise == 31:
    from src.exercicio31 import quebra_linhas
    quebra_linhas.quebra_linhas()
elif exercise == 32:
    from src.exercicio32 import sudoku
    sudoku.validar_sudoku()
