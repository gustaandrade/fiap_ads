#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

valor = input("Informe o valor bruto do pacote: ")
categoria = input("Informe a categoria dos assentos no vôo: ")
viajantes = input("Informe a quantidade de viajantes: ")
desconto = 0.0

try:
    valor = float(valor)
    categoria = categoria.upper()
    viajantes = int(viajantes)

    if categoria == "ECONÔMICA":
        if viajantes == 2:
            desconto = 0.03
        elif viajantes == 3:
            desconto = 0.04
        elif viajantes >= 4:
            desconto = 0.05
    elif categoria == "EXECUTIVA":
        if viajantes == 2:
            desconto = 0.05
        elif viajantes == 3:
            desconto = 0.07
        elif viajantes >= 4:
            desconto = 0.08
    elif categoria == "PRIMEIRA CLASSE":
        if viajantes == 2:
            desconto = 0.1
        elif viajantes == 3:
            desconto = 0.15
        elif viajantes >= 4:
            desconto = 0.2
    else:
        categoria = "inválida"

    if categoria == "inválida":
        print("Categoria inválida, por favor, tente novamente com valores corretos.")
    else:
        print(f"Valor bruto da viagem: R$ {valor:.2f}.\n"
              f"Valor do desconto: R$ {valor * desconto:.2f}.\n"
              f"Valor líquido da viagem: R$ {(valor - valor * desconto):.2f}.\n"
              f"Valor médio por viajante: R$ {((valor - valor * desconto) / viajantes):.2f}.\n")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
