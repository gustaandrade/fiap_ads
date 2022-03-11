#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

import math

peso = input("Informe o seu peso: ")
altura = input("Informe a sua altura: ")

try:
    imc = int(peso) / math.pow(float(altura.replace(",", ".")), 2)
    faixa = ""

    if imc < 16:
        faixa = "Baixo peso Grau III"
    elif 16 <= imc < 17:
        faixa = "Baixo peso Grau II"
    elif 17 <= imc < 18.5:
        faixa = "Baixo peso Grau I"
    elif 18.5 <= imc < 25:
        faixa = "Peso ideal"
    elif 25 <= imc < 30:
        faixa = "Sobrepeso"
    elif 30 <= imc < 35:
        faixa = "Obesidade Grau I"
    elif 35 <= imc < 40:
        faixa = "Obesidade Grau II"
    else:
        faixa = "Obesidade Grau III"

    print(f"O seu IMC é de aproximadamente {imc:.2f}, valor considerado na faixa {faixa}.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
