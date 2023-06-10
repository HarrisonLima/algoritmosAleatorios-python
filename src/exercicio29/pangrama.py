import string

def pangrama(frase):
    alfabeto = set(string.ascii_lowercase)

    frase = frase.lower()

    frase = frase.translate(str.maketrans("", "", string.punctuation))

    letras_presentes = set(frase)
    return letras_presentes == alfabeto

frase = input("Digite uma frase: ")

if pangrama(frase):
    print("A frase é um pangrama.")
else:
    print("A frase não é um pangrama.")
