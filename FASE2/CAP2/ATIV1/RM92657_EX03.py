#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

seg = input("Informe quantos votos recebeu a segunda-feira: ")
ter = input("Informe quantos votos recebeu a terça-feira: ")
qua = input("Informe quantos votos recebeu a quarta-feira: ")
qui = input("Informe quantos votos recebeu a quinta-feira: ")
sex = input("Informe quantos votos recebeu a sexta-feira: ")

try:
    seg = int(seg)
    ter = int(ter)
    qua = int(qua)
    qui = int(qui)
    sex = int(sex)

    if seg > ter and seg > qua and seg > qui and seg > sex:
        print(f"O dia escolhido foi segunda-feira, com o total de {seg} votos.")
    elif ter > seg and ter > qua and ter > qui and ter > sex:
        print(f"O dia escolhido foi terça-feira, com o total de {ter} votos.")
    elif qua > seg and qua > ter and qua > qui and qua > sex:
        print(f"O dia escolhido foi quarta-feira, com o total de {qua} votos.")
    elif qui > seg and qui > ter and qui > qua and qui > sex:
        print(f"O dia escolhido foi quinta-feira, com o total de {qui} votos.")
    elif sex > seg and sex > ter and sex > qua and sex > qui:
        print(f"O dia escolhido foi sexta-feira, com o total de {sex} votos.")

    elif seg == ter and seg > qua and seg > qui and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira e terça-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == qua and seg > ter and seg > qui and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira e quarta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == qui and seg > ter and seg > qua and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira e quinta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == sex and seg > ter and seg > qua and seg > qui:
        print(f"Os dias escolhidos foram segunda-feira e sexta-feira, "
              f"com o total de {seg} votos cada.")
    elif ter == qua and ter > seg and ter > qui and ter > sex:
        print(f"Os dias escolhidos foram terça-feira e quarta-feira, "
              f"com o total de {ter} votos cada.")
    elif ter == qui and ter > seg and ter > qua and ter > sex:
        print(f"Os dias escolhidos foram terça-feira e quinta-feira, "
              f"com o total de {ter} votos cada.")
    elif ter == sex and ter > seg and ter > qua and ter > qui:
        print(f"Os dias escolhidos foram terça-feira e sexta-feira, "
              f"com o total de {ter} votos cada.")
    elif qua == qui and qua > seg and qua > ter and qua > sex:
        print(f"Os dias escolhidos foram quarta-feira e quinta-feira, "
              f"com o total de {qua} votos cada.")
    elif qua == sex and qua > seg and qua > ter and qua > qui:
        print(f"Os dias escolhidos foram quarta-feira e sexta-feira, "
              f"com o total de {qua} votos cada.")
    elif qui == sex and qui > seg and qui > ter and qui > qua:
        print(f"Os dias escolhidos foram quinta-feira e sexta-feira, "
              f"com o total de {qui} votos cada.")

    elif seg == ter and seg == qua and seg > qui and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira e quarta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == ter and seg == qui and seg > ter and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira e quinta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == ter and seg == sex and seg > ter and seg > qui:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira e sexta-feira, "
              f"com o total de {seg} votos cada.")
    elif ter == qua and ter == qui and ter > seg and ter > sex:
        print(f"Os dias escolhidos foram terça-feira, quarta-feira e quinta-feira, "
              f"com o total de {ter} votos cada.")
    elif ter == qua and ter == sex and ter > seg and ter > qui:
        print(f"Os dias escolhidos foram terça-feira, quarta-feira e sexta-feira, "
              f"com o total de {ter} votos cada.")
    elif qua == qui and qua == sex and qua > seg and qua > ter:
        print(f"Os dias escolhidos foram quarta-feira, quinta-feira e sexta-feira, "
              f"com o total de {qua} votos cada.")
    elif seg == qua and seg == qui and seg > ter and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira, quarta-feira e quinta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == qua and seg == sex and seg > ter and seg > qui:
        print(f"Os dias escolhidos foram segunda-feira, quarta-feira e sexta-feira, "
              f"com o total de {seg} votos cada.")
    elif seg == qui and seg == sex and seg > ter and seg > qua:
        print(f"Os dias escolhidos foram segunda-feira, quinta-feira e sexta-feira, "
              f"com o total de {seg} votos cada.")
    elif ter == qui and ter == sex and ter > seg and ter > qua:
        print(f"Os dias escolhidos foram terça-feira, quinta-feira e sexta-feira, "
              f"com o total de {ter} votos cada.")

    elif seg == ter and seg == qua and seg == qui and seg > sex:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira, quarta-feira e "
              f"quinta-feira, com o total de {seg} votos cada.")
    elif ter == qua and ter == qui and ter == sex and ter > seg:
        print(f"Os dias escolhidos foram terça-feira, quarta-feira, quinta-feira e "
              f"sexta-feira, com o total de {ter} votos cada.")
    elif seg == qua and seg == qui and seg == sex and seg > ter:
        print(f"Os dias escolhidos foram segunda-feira, quarta-feira, quinta-feira e "
              f"sexta-feira, com o total de {seg} votos cada.")
    elif seg == ter and seg == qui and seg == sex and seg > qua:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira, quinta-feira e "
              f"sexta-feira, com o total de {seg} votos cada.")
    elif seg == ter and seg == qua and seg == sex and seg > qui:
        print(f"Os dias escolhidos foram segunda-feira, terça-feira, quarta-feira e "
              f"sexta-feira, com o total de {seg} votos cada.")

    elif seg == ter and seg == qua and seg == qui and seg == sex:
        print(f"Houve um empate entre todos os dias, com o total de {seg} votos cada.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
