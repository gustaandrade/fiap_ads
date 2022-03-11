#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

minutos = input("Digite os minutos atuais: ")

loopMinutos = minutos
fatorial = 1

try:
    minutos = int(minutos)
    loopMinutos = int(loopMinutos)

    while loopMinutos > 0:
        fatorial *= loopMinutos
        loopMinutos -= 1

    if minutos > 0:
        print(f"A senha para desbloquear o servidor é LIBERDADE{fatorial}.")
    else:
        print(f"Senha impossível para números negativos.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
