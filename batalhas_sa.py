import heapq
import math


def tempo_batalha(dificuldade, equipe, poder):
    poder_total = sum(poder[cavaleiro] for cavaleiro in equipe)
    if poder_total <= 0:
        raise ValueError("Equipe sem poder total valido para batalha.")
    return float(dificuldade) / poder_total


def _precomputar_subconjuntos(cavaleiros, poderes):
    subconjuntos = []
    quantidade = len(cavaleiros)

    for mascara in range(1, 1 << quantidade):
        indices = [indice for indice in range(quantidade) if mascara & (1 << indice)]
        poder_total = sum(poderes[indice] for indice in indices)
        subconjuntos.append((mascara, tuple(indices), poder_total))

    return subconjuntos


def _mascara_disponivel(energias):
    mascara = 0
    for indice, energia in enumerate(energias):
        if energia > 0:
            mascara |= 1 << indice
    return mascara


def _heuristica_tempo(indice_casa, energias, soma_dificuldades_restantes, poderes):
    if indice_casa >= len(soma_dificuldades_restantes) - 1:
        return 0.0

    poder_disponivel = sum(
        poderes[indice] for indice, energia in enumerate(energias) if energia > 0
    )
    if poder_disponivel <= 0:
        return math.inf

    dificuldade_restante = soma_dificuldades_restantes[indice_casa]
    return dificuldade_restante / poder_disponivel


def _reconstruir_plano(caminho_estado, estado_final, cavaleiros, dificuldades, poder):
    alocacao_mascaras = []
    atual = estado_final

    while atual in caminho_estado:
        estado_anterior, mascara_equipe = caminho_estado[atual]
        alocacao_mascaras.append(mascara_equipe)
        atual = estado_anterior

    alocacao_mascaras.reverse()

    resultados = []
    for indice, mascara in enumerate(alocacao_mascaras):
        equipe = tuple(
            cavaleiros[pos] for pos in range(len(cavaleiros)) if mascara & (1 << pos)
        )
        tempo = tempo_batalha(dificuldades[indice][1], equipe, poder)
        resultados.append((dificuldades[indice][0], equipe, tempo))

    return resultados


def _energia_final_por_estado(estado, cavaleiros):
    _, energias = estado
    return {cavaleiro: energias[indice] for indice, cavaleiro in enumerate(cavaleiros)}


def planejar_batalhas(dificuldades, poder, energia, energia_minima_final_total=0):
    cavaleiros = list(poder.keys())
    poderes = [float(poder[cavaleiro]) for cavaleiro in cavaleiros]
    numero_casas = len(dificuldades)

    if numero_casas == 0:
        return [], 0.0, dict(energia)

    energias_iniciais = tuple(int(energia.get(cavaleiro, 0)) for cavaleiro in cavaleiros)
    if any(valor < 0 for valor in energias_iniciais):
        raise ValueError("Energia inicial nao pode ser negativa.")

    energia_total_inicial = sum(energias_iniciais)

    if energia_total_inicial < numero_casas:
        raise ValueError("Energia total insuficiente para cobrir todas as casas.")

    if energia_minima_final_total < 0:
        raise ValueError("Energia minima final nao pode ser negativa.")

    if energia_total_inicial < numero_casas + energia_minima_final_total:
        raise ValueError(
            "Restricao de energia final inviavel com a energia inicial disponivel."
        )

    dificuldades_valores = [float(casa[1]) for casa in dificuldades]
    soma_dificuldades_restantes = [0.0] * (numero_casas + 1)
    for indice in range(numero_casas - 1, -1, -1):
        soma_dificuldades_restantes[indice] = (
            soma_dificuldades_restantes[indice + 1] + dificuldades_valores[indice]
        )

    subconjuntos = _precomputar_subconjuntos(cavaleiros, poderes)

    estado_inicial = (0, energias_iniciais)
    custo_inicial = 0.0
    h_inicial = _heuristica_tempo(
        estado_inicial[0], estado_inicial[1], soma_dificuldades_restantes, poderes
    )

    fronteira = [(custo_inicial + h_inicial, custo_inicial, estado_inicial)]
    melhor_custo = {estado_inicial: 0.0}
    caminho_estado = {}
    estado_objetivo = None
    custo_objetivo = None

    while fronteira:
        _, custo_atual, estado_atual = heapq.heappop(fronteira)

        if custo_atual > melhor_custo.get(estado_atual, math.inf):
            continue

        indice_casa, energias = estado_atual

        casas_restantes = numero_casas - indice_casa
        energia_total_atual = sum(energias)

        # Cada batalha restante consome no minimo 1 ponto total de energia.
        if energia_total_atual - casas_restantes < energia_minima_final_total:
            continue

        if indice_casa == numero_casas:
            if energia_total_atual >= energia_minima_final_total:
                estado_objetivo = estado_atual
                custo_objetivo = custo_atual
                break
            continue

        dificuldade = dificuldades_valores[indice_casa]
        disponivel = _mascara_disponivel(energias)

        if disponivel == 0:
            continue

        for mascara, indices, poder_total in subconjuntos:
            if mascara & ~disponivel:
                continue

            novas_energias = list(energias)
            for indice in indices:
                novas_energias[indice] -= 1

            proximo_estado = (indice_casa + 1, tuple(novas_energias))
            custo_transicao = dificuldade / poder_total
            novo_custo = custo_atual + custo_transicao

            if novo_custo >= melhor_custo.get(proximo_estado, math.inf):
                continue

            melhor_custo[proximo_estado] = novo_custo
            caminho_estado[proximo_estado] = (estado_atual, mascara)

            h = _heuristica_tempo(
                proximo_estado[0],
                proximo_estado[1],
                soma_dificuldades_restantes,
                poderes,
            )
            heapq.heappush(fronteira, (novo_custo + h, novo_custo, proximo_estado))

    if estado_objetivo is None:
        raise ValueError("Nao foi possivel planejar batalhas com a energia disponivel.")

    resultados = _reconstruir_plano(
        caminho_estado, estado_objetivo, cavaleiros, dificuldades, poder
    )
    energia_final = _energia_final_por_estado(estado_objetivo, cavaleiros)
    return resultados, custo_objetivo, energia_final
