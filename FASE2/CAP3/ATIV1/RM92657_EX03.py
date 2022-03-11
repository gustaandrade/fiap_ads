#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

valorTeste = input("Informe o número para a verificação da ação: ")

atualFibonacci = 1
anteriorFibonacci = 0
somaFibonacci = anteriorFibonacci + atualFibonacci

try:
    valorTeste = int(valorTeste)

    while atualFibonacci < valorTeste:
        somaFibonacci = atualFibonacci + anteriorFibonacci
        anteriorFibonacci = atualFibonacci
        atualFibonacci = somaFibonacci

    if valorTeste == atualFibonacci:
        print("Ação bem sucedida!")
    else:
        print("A ação falhou...")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
