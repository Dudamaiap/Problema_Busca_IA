import heapq


def calcular_heuristica(posicao_atual, objetivo):

    x1, y1 = posicao_atual
    x2, y2 = objetivo

    return abs(x1 - x2) + abs(y1 - y2)


def obter_vizinhos(posicao, mapa):

    x, y = posicao

    movimentos = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    vizinhos_validos = []

    for nx, ny in movimentos:
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]):
            vizinhos_validos.append((nx, ny))

    return vizinhos_validos


def calcular_caminho_a_estrela(mapa, inicio, objetivo, custo_terreno):

    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))

    veio_de = {}
    custo_ate = {inicio: 0.0}

    while fila_prioridade:

        atual = heapq.heappop(fila_prioridade)[1]

        if atual == objetivo:
            break

        for vizinho in obter_vizinhos(atual, mapa):

            tipo_terreno = mapa[vizinho[0]][vizinho[1]]
            custo_entrada = custo_terreno[str(tipo_terreno)]

            custo = custo_ate[atual] + custo_entrada

            if vizinho not in custo_ate or custo < custo_ate[vizinho]:

                custo_ate[vizinho] = custo
                prioridade = custo + calcular_heuristica(vizinho, objetivo)

                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                veio_de[vizinho] = atual

    caminho = []
    atual = objetivo

    while atual != inicio:
        caminho.append(atual)
        atual = veio_de[atual]

    caminho.append(inicio)
    caminho.reverse()

    return caminho, custo_ate[objetivo]