import tkinter as tk


class InterfaceGrafica:
    def __init__(self, mapa, caminho, marcos=None):

        self.mapa = mapa
        self.caminho = list(caminho or [])
        self.marcos = marcos or {}

        self.indice_animacao = 0
        self.agente_id = None

        # tamanho automático
        self.tamanho = max(10, 900 // len(self.mapa))

        self.janela = tk.Tk()
        self.janela.title("⚔️ Cavaleiros do Zodíaco - Busca Inteligente")

        largura = len(self.mapa[0]) * self.tamanho
        altura = len(self.mapa) * self.tamanho

        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        self.canvas = tk.Canvas(
            self.frame,
            width=largura,
            height=altura,
            bg="#111"
        )
        self.canvas.grid(row=0, column=0)

        self.info = tk.Label(
            self.frame,
            text="Iniciando...",
            font=("Arial", 11, "bold"),
            bg="#222",
            fg="white",
            width=30
        )
        self.info.grid(row=0, column=1, sticky="ns")

        self._desenhar_mapa()
        self._desenhar_caminho()
        self._desenhar_marcos()
        self._desenhar_legenda()

        self._animar_agente()

        self.janela.mainloop()

    # ----------------------------------
    # MAPA
    # ----------------------------------

    def _desenhar_mapa(self):

        cores = {

            0: "#ff5252",      # inicio
            13: "#00e676",     # objetivo
            14: "#37474f",     # montanhoso
            15: "#eeeeee",     # plano
            16: "#90a4ae",     # rochoso

        }

        for linha, valores in enumerate(self.mapa):

            for coluna, codigo in enumerate(valores):

                if 1 <= codigo <= 12:
                    cor = "#ffd54f"
                else:
                    cor = cores.get(codigo, "#ffffff")

                x1 = coluna * self.tamanho
                y1 = linha * self.tamanho

                x2 = x1 + self.tamanho
                y2 = y1 + self.tamanho

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=cor,
                    outline="#1a1a1a",
                    width=0.4
                )

    # ----------------------------------
    # CAMINHO
    # ----------------------------------

    def _desenhar_caminho(self):

        if not self.caminho:
            return

        pontos = []

        for linha, coluna in self.caminho:

            x = coluna * self.tamanho + self.tamanho / 2
            y = linha * self.tamanho + self.tamanho / 2

            pontos.extend((x, y))

        self.canvas.create_line(
            *pontos,
            fill="#2196f3",
            width=max(2, self.tamanho // 3),
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND
        )

    # ----------------------------------
    # MARCOS (CASAS)
    # ----------------------------------

    def _desenhar_marcos(self):

        for codigo, (linha, coluna) in self.marcos.items():

            if codigo == 0:
                texto = "S"
            elif codigo == 13:
                texto = "G"
            else:
                texto = str(codigo)

            self.canvas.create_text(
                coluna * self.tamanho + self.tamanho / 2,
                linha * self.tamanho + self.tamanho / 2,
                text=texto,
                fill="black",
                font=("Arial", max(8, self.tamanho // 2), "bold"),
            )

    # ----------------------------------
    # LEGENDA
    # ----------------------------------

    def _desenhar_legenda(self):

        legenda = """

Legenda

S = Entrada
G = Grande Mestre

Amarelo = Casas

Cinza claro = Plano
Cinza = Rochoso
Cinza escuro = Montanhoso

Linha azul = Caminho
Círculo vermelho = Agente
"""

        self.info.config(text=legenda)

    # ----------------------------------
    # ANIMAÇÃO
    # ----------------------------------

    def _animar_agente(self):

        if not self.caminho:
            return

        linha, coluna = self.caminho[self.indice_animacao]

        margem = max(2, self.tamanho // 5)

        if self.agente_id:
            self.canvas.delete(self.agente_id)

        self.agente_id = self.canvas.create_oval(

            coluna * self.tamanho + margem,
            linha * self.tamanho + margem,

            coluna * self.tamanho + self.tamanho - margem,
            linha * self.tamanho + self.tamanho - margem,

            fill="#ff1744",
            outline="white",
            width=1
        )

        self.janela.title(
            f"Cavaleiros do Zodíaco - Passo {self.indice_animacao+1}/{len(self.caminho)}"
        )

        if self.indice_animacao < len(self.caminho) - 1:

            self.indice_animacao += 1
            self.janela.after(40, self._animar_agente)