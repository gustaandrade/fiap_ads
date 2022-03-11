#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

bpm = input("Informe o seu número de batimentos por minuto (BPM): ")
idade = input("Informe a sua idade: ")

try:
    bpm = int(bpm)
    idade = int(idade)

    if idade <= 2:
        if bpm < 120:
            print("ABAIXO da faixa adequada")
        elif bpm > 140:
            print("ACIMA da faixa adequada")
        else:
            print("DENTRO da faixa adequada")
    elif 8 <= idade <= 17:
        if bpm < 80:
            print("ABAIXO da faixa adequada")
        elif bpm > 100:
            print("ACIMA da faixa adequada")
        else:
            print("DENTRO da faixa adequada")
    elif 18 <= idade <= 65:
        if bpm < 70:
            print("ABAIXO da faixa adequada")
        elif bpm > 80:
            print("ACIMA da faixa adequada")
        else:
            print("DENTRO da faixa adequada")
    elif idade > 65:
        if bpm < 50:
            print("ABAIXO da faixa adequada")
        elif bpm > 60:
            print("ACIMA da faixa adequada")
        else:
            print("DENTRO da faixa adequada")
    else:
        print("Idade fora da faixa de cálculo")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
