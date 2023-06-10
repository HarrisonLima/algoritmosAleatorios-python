def primo(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

num = int(input("Digite um número: "))

if primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

if __name__ == '__main__':
    primo()