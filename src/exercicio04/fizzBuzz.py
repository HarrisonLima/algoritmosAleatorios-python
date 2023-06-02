def FizzBuzz():
    start = int(input("Informe o número inicial: "))
    end = int(input("Informe o número final: "))

    if end <= start:
        print("O número final deve ser maior que o número inicial.")
        return

    for i in range(start, end+1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(i)
        print(output)
