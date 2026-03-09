import csv


def carregar_legenda_terrenos(caminho_arquivo):

    legenda = {}

    with open(caminho_arquivo) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            numero = linha[0]
            nome = linha[1]

            legenda[numero] = nome

    return legenda


def carregar_mapa(caminho_arquivo):

    mapa = []

    with open(caminho_arquivo) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            mapa.append([int(valor) for valor in linha])

    return mapa


def carregar_dicionario(caminho_arquivo):

    dados = {}

    with open(caminho_arquivo) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            chave = linha[0]
            valor = float(linha[1])

            dados[chave] = valor

    return dados


def carregar_lista(caminho_arquivo):

    lista = []

    with open(caminho_arquivo) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:
            lista.append((linha[0], float(linha[1])))

    return lista