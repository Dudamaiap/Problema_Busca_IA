from tkinter import TclError

from carregar_dados import (
    carregar_mapa,
    carregar_dicionario,
    carregar_lista,
    carregar_legenda_terrenos,
)

from busca_caminho import calcular_rota_por_marcos
from batalhas_sa import planejar_batalhas
from interface import InterfaceGrafica


MAPA_ARQUIVO = "CSV's/mapa.csv"
VALOR_TERRENOS_ARQUIVO = "CSV's/valor_terrenos.csv"
PODER_CAVALEIRO_ARQUIVO = "CSV's/poder_cavaleiro.csv"
DIFICULDADE_CASA_ARQUIVO = "CSV's/dificuldade_casa.csv"
LEGENDA_TERRENO_ARQUIVO = "CSV's/legenda_terreno.csv"
ENERGIA_MINIMA_FINAL_TOTAL = 1


def montar_custos_por_codigo(legenda, custos_nome):
    custos = {}

    for codigo, nome in legenda.items():
        custos[int(codigo)] = float(custos_nome.get(nome, 1.0))

    return custos


def converter_mapa(mapa, custos):
    mapa_custo = []

    for linha in mapa:
        nova = []

        for valor in linha:
            nova.append(custos.get(valor, 1.0))

        mapa_custo.append(nova)

    return mapa_custo


def encontrar_marcos(mapa, codigos):
    encontrados = {}

    for linha, valores in enumerate(mapa):
        for coluna, codigo in enumerate(valores):
            if codigo in codigos:
                if codigo in encontrados:
                    raise ValueError(
                        f"Codigo {codigo} aparece mais de uma vez no mapa."
                    )
                encontrados[codigo] = (linha, coluna)

    faltando = [codigo for codigo in codigos if codigo not in encontrados]
    if faltando:
        raise ValueError(f"Codigos obrigatorios ausentes no mapa: {faltando}")

    return encontrados


def main():
    mapa = carregar_mapa(MAPA_ARQUIVO)

    custo_nome = carregar_dicionario(VALOR_TERRENOS_ARQUIVO)
    legenda = carregar_legenda_terrenos(LEGENDA_TERRENO_ARQUIVO)
    custo_terreno = montar_custos_por_codigo(legenda, custo_nome)
    mapa_custo = converter_mapa(mapa, custo_terreno)

    poderes = carregar_dicionario(PODER_CAVALEIRO_ARQUIVO)
    dificuldades = sorted(carregar_lista(DIFICULDADE_CASA_ARQUIVO), key=lambda item: item[0])

    energia = {c: 5 for c in poderes}

    marcos = encontrar_marcos(mapa, list(range(14)))
    rota_obrigatoria = [marcos[codigo] for codigo in range(14)]

    caminho, custo_caminho = calcular_rota_por_marcos(mapa_custo, rota_obrigatoria)

    print("\n=== Resultado da Missao ===")
    print(f"Caminho percorrido (coordenadas): {caminho}")
    print(f"Passos: {len(caminho) - 1}")
    print(f"Custo total do caminho: {custo_caminho:.2f} minutos")

    batalhas, tempo_batalhas, energia_final = planejar_batalhas(
        dificuldades,
        poderes,
        energia,
        energia_minima_final_total=ENERGIA_MINIMA_FINAL_TOTAL,
    )

    print("\n=== Plano de Batalhas ===")
    for casa, equipe, tempo in batalhas:
        nomes = ", ".join(equipe)
        print(f"Casa {casa}: equipe [{nomes}] -> {tempo:.2f} minutos")

    tempo_total = custo_caminho + tempo_batalhas
    limite = 12 * 60

    print(f"\nTempo total batalhas: {tempo_batalhas:.2f} minutos")
    print(f"Energia restante: {energia_final}")
    print(f"Restricao: energia final total >= {ENERGIA_MINIMA_FINAL_TOTAL}")
    print(f"Tempo total da missao: {tempo_total:.2f} minutos")
    print(f"Limite de 12 horas: {limite} minutos")
    if tempo_total <= limite:
        print("Status: Atena foi salva dentro do limite.")
    else:
        print("Status: Missao falhou no limite de 12 horas.")

    try:
        InterfaceGrafica(mapa, caminho, marcos)
    except TclError:
        print("Sem interface gráfica")


if __name__ == "__main__":
    main()
