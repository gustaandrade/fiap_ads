#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

numeroTransacoes = input("Informe o número de transações que você fez hoje: ")

transacaoAtual = 0
somaTransacoes = 0
loopCount = 0

try:
    numeroTransacoes = int(numeroTransacoes)

    while loopCount < numeroTransacoes:
        transacaoAtual = float(input(f"Informe a transação de número {loopCount + 1}: ")
                               .replace(",", "."))
        somaTransacoes += transacaoAtual
        loopCount += 1

    print(f"O valor total gasto hoje é de R$ {somaTransacoes:.2f}.")
    print(f"A média do valor gasto hoje é de R$ {(somaTransacoes / numeroTransacoes):.2f}.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
