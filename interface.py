import tkinter as tk


class InterfaceGrafica:
    def __init__(self, mapa, caminho, marcos=None):
        self.mapa = mapa
        self.caminho = list(caminho or [])
        self.marcos = marcos or {}
        self.tamanho = 15
        self.indice_animacao = 0
        self.agente_id = None

        self.janela = tk.Tk()
        self.janela.title("Cavaleiros do Zodiaco - Busca")

        largura = len(self.mapa[0]) * self.tamanho
        altura = len(self.mapa) * self.tamanho
        self.canvas = tk.Canvas(self.janela, width=largura, height=altura)
        self.canvas.pack()

        self._desenhar_mapa()
        self._desenhar_caminho()
        self._desenhar_marcos()
        self._animar_agente()

        self.janela.mainloop()

    def _desenhar_mapa(self):
        cores = {
            0: "#ff4d4d",
            13: "#4caf50",
            14: "#5f6368",
            15: "#e0e0e0",
            16: "#9e9e9e",
        }

        for linha, valores in enumerate(self.mapa):
            for coluna, codigo in enumerate(valores):
                if 1 <= codigo <= 12:
                    cor = "#f6c343"
                else:
                    cor = cores.get(codigo, "white")

                self.canvas.create_rectangle(
                    coluna * self.tamanho,
                    linha * self.tamanho,
                    coluna * self.tamanho + self.tamanho,
                    linha * self.tamanho + self.tamanho,
                    fill=cor,
                    outline="#222",
                    width=0.25,
                )

    def _desenhar_caminho(self):
        if not self.caminho:
            return

        if len(self.caminho) == 1:
            linha, coluna = self.caminho[0]
            self.canvas.create_oval(
                coluna * self.tamanho + 4,
                linha * self.tamanho + 4,
                coluna * self.tamanho + self.tamanho - 4,
                linha * self.tamanho + self.tamanho - 4,
                fill="#1e88e5",
                outline="",
            )
            return

        pontos = []
        for linha, coluna in self.caminho:
            centro_x = coluna * self.tamanho + self.tamanho / 2
            centro_y = linha * self.tamanho + self.tamanho / 2
            pontos.extend((centro_x, centro_y))

        self.canvas.create_line(
            *pontos,
            fill="#0d47a1",
            width=max(2, self.tamanho // 3),
            capstyle=tk.ROUND,
            joinstyle=tk.ROUND,
        )

    def _desenhar_marcos(self):
        for codigo, (linha, coluna) in self.marcos.items():
            texto = str(codigo)
            if codigo == 0:
                texto = "S"
            elif codigo == 13:
                texto = "G"

            self.canvas.create_text(
                coluna * self.tamanho + self.tamanho / 2,
                linha * self.tamanho + self.tamanho / 2,
                text=texto,
                fill="black",
                font=("Arial", 8, "bold"),
            )

    def _animar_agente(self):
        if not self.caminho:
            return

        linha, coluna = self.caminho[self.indice_animacao]
        margem = max(2, self.tamanho // 5)

        if self.agente_id is not None:
            self.canvas.delete(self.agente_id)

        self.agente_id = self.canvas.create_oval(
            coluna * self.tamanho + margem,
            linha * self.tamanho + margem,
            coluna * self.tamanho + self.tamanho - margem,
            linha * self.tamanho + self.tamanho - margem,
            fill="#e53935",
            outline="white",
            width=1,
        )

        if self.indice_animacao < len(self.caminho) - 1:
            self.indice_animacao += 1
            self.janela.after(35, self._animar_agente)
