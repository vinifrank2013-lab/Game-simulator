
import random

participantes = []
paises = []


def adicionar_participantes():
    print("Ok, vamos adicionar os participantes")
    print("Quantos participantes vc vai adicionar?")
    nParticipantes = int(input())

    for participante in range(nParticipantes):
        print("Escreva o nome do participante")
        nomeparticipante = str(input())
        participantes.append(nomeparticipante)

    return nParticipantes


def adicionar_paises():
    print("Vamos adicionar os Paises")

    for pais in range(nParticipantes):
        print("Escreva o país")
        nomepais = str(input())
        paises.append(nomepais)


def escolher_paises():
    random.shuffle(paises)

    for participante2 in range(nParticipantes):
        print(f"Participante: {participantes[participante2]} - País: {paises[participante2]}")


nParticipantes = 0

while True:
    print("MENU")
    print("1. Determinar participantes")
    print("2. Determinar Países")
    print("3. Determinar os países dos participantes (aleatoriamente)")
    print("4. Sair")

    op = int(input())

    if op == 1:
        nParticipantes = adicionar_participantes()

    elif op == 2:
        adicionar_paises()

    elif op == 3:
        escolher_paises()

    elif op == 4:
        break

    else:
        print("Opção inválida, tente denovo.")

