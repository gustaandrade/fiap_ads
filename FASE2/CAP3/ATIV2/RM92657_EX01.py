#####################################################
#   Análise e Desenvolvimento de Sistemas - FIAP    #
#       Gustavo Andrade Guimarães - RM 92657        #
#####################################################

somaImpar = 0
somaPar = 0

loopCountImpar = 1
loopCountPar = 2

totalAlunos = 50

try:
    while loopCountImpar < totalAlunos:
        print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
        nota = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {loopCountImpar}: ")
                   .replace(",", "."))
        somaImpar += nota
        loopCountImpar += 2

    while loopCountPar <= totalAlunos:
        print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
        nota = int(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {loopCountPar}: ")
                   .replace(",", "."))
        somaPar += nota
        loopCountPar += 2

    print(f"A média da turma ímpar é de {float(somaImpar / (totalAlunos / 2))}.")
    print(f"A média da turma par é de {float(somaPar / (totalAlunos / 2))}.")

    if somaImpar > somaPar:
        print("A turma ímpar teve a maior nota.")
    elif somaPar > somaImpar:
        print("A turma par teve a maior nota.")
    else:
        print("As duas turmas tiveram a mesma nota.")

except ValueError:
    print("Ops, valores inválidos foram inseridos. Por favor, tente novamente.")
