#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

numeroAlimentos = input("Informe o número de alimentos que inseriu hoje: ")

alimentoAtual = 0
somaCalorias = 0
loopCount = 0

try:
    numeroAlimentos = int(numeroAlimentos)

    while loopCount < numeroAlimentos:
        alimentoAtual = float(input(f"Informe as calorias do alimento {loopCount + 1}: ")
                              .replace(",", "."))
        somaCalorias += alimentoAtual
        loopCount += 1

    print(f"A soma de calorias ingeridas no dia de hoje é {somaCalorias} cal.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
