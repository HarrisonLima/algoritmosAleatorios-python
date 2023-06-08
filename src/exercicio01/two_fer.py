def two_fer(name="você"):
    return f"Um para {name}, um para mim."

name = input("Digite um nome (ou pressione Enter para nenhum nome): ")
if not name:
    name = "você"
result = two_fer(name)
print(result)

if __name__ == '__main__':
    two_fer()
