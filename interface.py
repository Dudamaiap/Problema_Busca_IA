import tkinter as tk


class InterfaceGrafica:

    def __init__(self, mapa, caminho):

        self.mapa = mapa
        self.caminho = caminho

        self.tamanho = 15

        self.janela = tk.Tk()
        self.janela.title("Cavaleiros do Zodíaco")

        largura = len(mapa[0]) * self.tamanho
        altura = len(mapa) * self.tamanho

        self.canvas = tk.Canvas(self.janela, width=largura, height=altura)
        self.canvas.pack()

        self.desenhar_mapa()

        self.indice = 0

        self.janela.after(200, self.animar)

        self.janela.mainloop()


    def obter_cor(self, valor):

        if valor == 14:
            return "#d9d9d9"

        if valor == 15:
            return "#888888"

        if valor == 16:
            return "#444444"

        return "white"


    def desenhar_mapa(self):

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):

                valor = self.mapa[i][j]
                cor = self.obter_cor(valor)

                x1 = j * self.tamanho
                y1 = i * self.tamanho

                x2 = x1 + self.tamanho
                y2 = y1 + self.tamanho

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor)


    def animar(self):

        if self.indice >= len(self.caminho):
            return

        x, y = self.caminho[self.indice]

        x1 = y * self.tamanho
        y1 = x * self.tamanho

        x2 = x1 + self.tamanho
        y2 = y1 + self.tamanho

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")

        self.indice += 1

        self.janela.after(50, self.animar)