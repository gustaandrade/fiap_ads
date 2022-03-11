#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

voto1 = input("Digite o primeiro voto (opções possíveis: PLAYSTATION, XBOX ou NINTENDO): ")
voto2 = input("Digite o segundo voto (opções possíveis: PLAYSTATION, XBOX ou NINTENDO): ")
voto3 = input("Digite o terceiro voto (opções possíveis: PLAYSTATION, XBOX ou NINTENDO): ")
voto4 = input("Digite o quarto voto (opções possíveis: PLAYSTATION, XBOX ou NINTENDO): ")
voto5 = input("Digite o quinto voto (opções possíveis: PLAYSTATION, XBOX ou NINTENDO): ")

playstation = 0
xbox = 0
nintendo = 0

try:
    voto1 = voto1.upper()
    voto2 = voto2.upper()
    voto3 = voto3.upper()
    voto4 = voto4.upper()
    voto5 = voto5.upper()

    if voto1 == "PLAYSTATION":
        playstation += 1
    elif voto1 == "XBOX":
        xbox += 1
    elif voto1 == "NINTENDO":
        nintendo += 1

    if voto2 == "PLAYSTATION":
        playstation += 1
    elif voto2 == "XBOX":
        xbox += 1
    elif voto2 == "NINTENDO":
        nintendo += 1

    if voto3 == "PLAYSTATION":
        playstation += 1
    elif voto3 == "XBOX":
        xbox += 1
    elif voto3 == "NINTENDO":
        nintendo += 1

    if voto4 == "PLAYSTATION":
        playstation += 1
    elif voto4 == "XBOX":
        xbox += 1
    elif voto4 == "NINTENDO":
        nintendo += 1

    if voto5 == "PLAYSTATION":
        playstation += 1
    elif voto5 == "XBOX":
        xbox += 1
    elif voto5 == "NINTENDO":
        nintendo += 1

    if playstation > xbox and playstation > nintendo:
        print("A opção vencedora foi PLAYSTATION.")
    elif xbox > playstation and xbox > nintendo:
        print("A opção vencedora foi XBOX.")
    elif nintendo > playstation and nintendo > xbox:
        print("A opção vencedora foi NINTENDO.")
    elif playstation == xbox and playstation > nintendo:
        print("Houve um empate entre as opções PLAYSTATION e XBOX.")
    elif playstation == nintendo and playstation > xbox:
        print("Houve um empate entre as opções PLAYSTATION e NINTENDO.")
    elif xbox == nintendo and xbox > playstation:
        print("Houve um empate entre as opções XBOX e NINTENDO.")
    elif playstation == xbox and playstation == nintendo:
        print("Houve um empate entre todas as opções.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
