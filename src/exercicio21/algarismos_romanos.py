def algarismos_romanos(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for symbol in roman_numeral[::-1]:
        value = roman_values[symbol]

        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total

numeral_romano = input("Digite um numeral romano: ")
numero_inteiro = algarismos_romanos(numeral_romano.upper())
print("O numeral romano", numeral_romano, "corresponde ao número inteiro", numero_inteiro)