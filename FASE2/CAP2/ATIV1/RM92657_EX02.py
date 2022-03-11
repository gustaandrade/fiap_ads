#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

assinatura = input("Informe o nome da sua assinatura: ").upper()
faturamento = input("Informe o seu faturamento (em reais): ")

try:
    faturamento = float(faturamento.replace(",", "."))

    if assinatura == "BASIC":
        print(f"O bônus que sua empresa precisa pagar é de R$ {(faturamento * 0.3):.2f}.")
    elif assinatura == "SILVER":
        print(f"O bônus que sua empresa precisa pagar é de R$ {(faturamento * 0.2):.2f}.")
    elif assinatura == "GOLD":
        print(f"O bônus que sua empresa precisa pagar é de R$ {(faturamento * 0.1):.2f}.")
    elif assinatura == "PLATINUM":
        print(f"O bônus que sua empresa precisa pagar é de R$ {(faturamento * 0.05):.2f}.")
    else:
        print("Sua assinatura não foi reconhecida. Por favor, tente novamente.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
