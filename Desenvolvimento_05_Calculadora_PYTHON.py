print("Olá qual operação você deseja realizar?")
print("1- Soma")
print("2- Subtração")
print("3- Divisão")
print("4- Multiplicação\n\n")
escolha = int(input("Digite o número correspondente: "))
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
if escolha == 1:
    resultado = valor1 + valor2
    resultado = "soma foi: {}".format(resultado)
elif escolha == 2:
    resultado = valor1 - valor2
    resultado = "subtração foi: {}".format(resultado)
elif escolha == 3:
    resultado = valor1 / valor2
    resultado = "divisão foi: {}".format(resultado)
else:
    resultado = valor1 * valor2
    resultado = "multiplicação foi: {}".format(resultado)

print("O resultado da {}".format(resultado))
