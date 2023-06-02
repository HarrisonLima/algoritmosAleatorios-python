def TwoFer(name="você"):
    return f"Um para {name}, um para mim."

name = input("Digite um nome (ou pressione Enter para nenhum nome): ")
if not name:
    name = "você"
result = TwoFer(name)
print(result)
