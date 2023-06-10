def anagrama(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    if len(string1) != len(string2):
        return False

    contador = {}

    for letra in string1:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

    for letra in string2:
        if letra in contador:
            contador[letra] -= 1
        else:
            return False

    return all(value == 0 for value in contador.values())

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if anagrama(string1, string2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")
