#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#                  Desafio iFood                    #
#                                                   #
#           Giovanne Pinto de Siqueira              #
#            Gustavo Andrade Guimarães              #
#                Nathalia Menezes                   #
#####################################################

restaurantes = ["O Mineiro",
                "Amor aos Pedaços",
                "We Coffee",
                "Lamen Kazu",
                "Mr. Pretzels",
                "Brigaderia Shopping Paulista"]
avaliacoes = [4.2, 4.3, 4.5, 4.8, 4.7, 4.7]
distancias = [1.7, 1.2, 0.8, 0.7, 1.1, 1.2]

listaOrdenada = []
loopIndex = 0

while loopIndex < len(avaliacoes):
    maior = avaliacoes[0]
    maiorIndex = 0

    for index, aval in enumerate(avaliacoes):
        if aval > maior:
            maior = aval
            maiorIndex = index
        elif aval == maior:
            if distancias[index] <= distancias[maiorIndex]:
                maior = aval
                maiorIndex = index

    listaOrdenada.append(maiorIndex)
    avaliacoes[maiorIndex] = 0.0

    loopIndex += 1

print("Olá, suas recomendações ordenadas de restaurantes são:")
print(f"{restaurantes[listaOrdenada[0]]}")
print(f"{restaurantes[listaOrdenada[1]]}")
print(f"{restaurantes[listaOrdenada[2]]}")
print(f"{restaurantes[listaOrdenada[3]]}")
print(f"{restaurantes[listaOrdenada[4]]}")
print(f"{restaurantes[listaOrdenada[5]]}")
