import itertools


def planejar_batalhas(dificuldade_casas, cavaleiros, energia):

    resultados = []
    tempo_total = 0

    for casa, dificuldade in dificuldade_casas:

        melhor_tempo = float("inf")
        melhor_equipe = None

        nomes = list(cavaleiros.keys())

        for tamanho in range(1, len(nomes) + 1):

            for equipe in itertools.combinations(nomes, tamanho):

                valido = True

                for cavaleiro in equipe:
                    if energia[cavaleiro] <= 0:
                        valido = False

                if not valido:
                    continue

                poder_total = sum(cavaleiros[c] for c in equipe)

                tempo = dificuldade / poder_total

                if tempo < melhor_tempo:

                    melhor_tempo = tempo
                    melhor_equipe = equipe

        for cavaleiro in melhor_equipe:
            energia[cavaleiro] -= 1

        resultados.append((casa, melhor_equipe, melhor_tempo))
        tempo_total += melhor_tempo

    return resultados, tempo_total, energia