import heapq
import math


MOVIMENTOS_CARDINAIS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def heuristica_manhattan(origem, destino, min_custo):
    distancia = abs(origem[0] - destino[0]) + abs(origem[1] - destino[1])
    return distancia * min_custo


def vizinhos_cardinais(posicao, linhas, colunas):
    x, y = posicao
    for dx, dy in MOVIMENTOS_CARDINAIS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < linhas and 0 <= ny < colunas:
            yield nx, ny


def _reconstruir_caminho(veio_de, inicio, objetivo):
    caminho = [objetivo]
    atual = objetivo

    while atual != inicio:
        atual = veio_de[atual]
        caminho.append(atual)

    caminho.reverse()
    return caminho


def _validar_mapa(mapa):
    if not mapa or not mapa[0]:
        raise ValueError("Mapa vazio.")

    colunas = len(mapa[0])
    if any(len(linha) != colunas for linha in mapa):
        raise ValueError("Mapa invalido: matriz irregular.")


def _validar_posicao(posicao, linhas, colunas, nome):
    if not (0 <= posicao[0] < linhas and 0 <= posicao[1] < colunas):
        raise ValueError(f"{nome} fora do mapa: {posicao}.")


def calcular_caminho_a_estrela(mapa, inicio, objetivo):
    _validar_mapa(mapa)

    linhas = len(mapa)
    colunas = len(mapa[0])

    _validar_posicao(inicio, linhas, colunas, "Posicao inicial")
    _validar_posicao(objetivo, linhas, colunas, "Posicao objetivo")

    if inicio == objetivo:
        return [inicio], 0.0

    min_custo = min(min(linha) for linha in mapa)

    fronteira = []
    custo_inicial = 0.0
    f_inicial = heuristica_manhattan(inicio, objetivo, min_custo)
    heapq.heappush(fronteira, (f_inicial, custo_inicial, inicio))

    melhor_custo = {inicio: custo_inicial}
    veio_de = {}

    while fronteira:
        _, custo_atual, atual = heapq.heappop(fronteira)

        if custo_atual > melhor_custo.get(atual, math.inf):
            continue

        if atual == objetivo:
            caminho = _reconstruir_caminho(veio_de, inicio, objetivo)
            return caminho, custo_atual

        for vizinho in vizinhos_cardinais(atual, linhas, colunas):
            nx, ny = vizinho
            custo_vizinho = custo_atual + float(mapa[nx][ny])

            if custo_vizinho >= melhor_custo.get(vizinho, math.inf):
                continue

            melhor_custo[vizinho] = custo_vizinho
            veio_de[vizinho] = atual

            h_vizinho = heuristica_manhattan(vizinho, objetivo, min_custo)
            heapq.heappush(
                fronteira,
                (custo_vizinho + h_vizinho, custo_vizinho, vizinho),
            )

    raise ValueError("Nao foi possivel encontrar caminho ate o objetivo.")


def calcular_rota_por_marcos(mapa, marcos):
    if not marcos:
        raise ValueError("Lista de marcos vazia.")

    if len(marcos) == 1:
        return [marcos[0]], 0.0

    caminho_total = []
    custo_total = 0.0

    for indice in range(len(marcos) - 1):
        inicio = marcos[indice]
        objetivo = marcos[indice + 1]
        caminho_trecho, custo_trecho = calcular_caminho_a_estrela(mapa, inicio, objetivo)

        if indice == 0:
            caminho_total.extend(caminho_trecho)
        else:
            caminho_total.extend(caminho_trecho[1:])

        custo_total += custo_trecho

    return caminho_total, custo_total
