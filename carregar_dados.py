import csv


def carregar_mapa(caminho):

    mapa = []

    with open(caminho) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            mapa.append([int(v) for v in linha])

    return mapa


def carregar_dicionario(caminho):

    dados = {}

    with open(caminho) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            dados[linha[0]] = float(linha[1])

    return dados


def carregar_lista(caminho):

    lista = []

    with open(caminho) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            lista.append((int(linha[0]), float(linha[1])))

    return lista


def carregar_legenda_terrenos(caminho):

    legenda = {}

    with open(caminho) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            legenda[linha[0]] = linha[1]

    return legenda