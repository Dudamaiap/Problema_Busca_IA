from tkinter import TclError

from carregar_dados import (
    carregar_dicionario,
    carregar_legenda_terrenos,
    carregar_lista,
    carregar_mapa,
)

from busca_caminho import calcular_caminho_a_estrela
from plano_batalha import planejar_batalhas
from interface import InterfaceGrafica


MAPA_ARQUIVO = "CSV's/mapa.csv"
VALOR_TERRENOS_ARQUIVO = "CSV's/valor_terrenos.csv"
PODER_CAVALEIRO_ARQUIVO = "CSV's/poder_cavaleiro.csv"
DIFICULDADE_CASA_ARQUIVO = "CSV's/dificuldade_casa.csv"
LEGENDA_TERRENO_ARQUIVO = "CSV's/legenda_terreno.csv"


def montar_custos_por_codigo(legenda, custos_nome):

    custos = {}

    for codigo, nome in legenda.items():
        custos[codigo] = custos_nome[nome]

    return custos


def main():

    mapa = carregar_mapa(MAPA_ARQUIVO)

    custo_terrenos_nome = carregar_dicionario(VALOR_TERRENOS_ARQUIVO)
    legenda_terreno = carregar_legenda_terrenos(LEGENDA_TERRENO_ARQUIVO)
    custo_terrenos = montar_custos_por_codigo(legenda_terreno, custo_terrenos_nome)

    poder_cavaleiros = carregar_dicionario(PODER_CAVALEIRO_ARQUIVO)
    dificuldade_casas = carregar_lista(DIFICULDADE_CASA_ARQUIVO)

    energia_inicial = {cavaleiro: 5 for cavaleiro in poder_cavaleiros}

    inicio = (41, 40)
    objetivo = (0, 35)

    caminho, custo = calcular_caminho_a_estrela(mapa, inicio, objetivo, custo_terrenos)

    print("Custo total do caminho:", custo)

    resultados_batalhas, tempo_total, energia_final = planejar_batalhas(
        dificuldade_casas,
        poder_cavaleiros,
        energia_inicial,
    )

    for casa, equipe, tempo in resultados_batalhas:
        print("\nCasa:", casa)
        print("Equipe:", equipe)
        print("Tempo:", tempo)

    print("\nTempo total de batalhas:", tempo_total)
    print("Energia restante:", energia_final)

    try:
        InterfaceGrafica(mapa, caminho)
    except TclError:
        print("Interface gráfica indisponível.")


if __name__ == "__main__":
    main()