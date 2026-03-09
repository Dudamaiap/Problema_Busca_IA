# Problema_Busca_IA

## Descrição

Este projeto implementa um **agente inteligente** capaz de guiar os Cavaleiros de Bronze pelo **Santuário das 12 Casas do Zodíaco** para salvar Atena.

O agente precisa resolver **dois problemas principais**:

1. **Encontrar o caminho de menor custo no mapa do santuário**
2. **Planejar quais cavaleiros lutarão em cada casa do zodíaco**

O objetivo é minimizar o **tempo total da missão**, considerando:

* custo de movimentação no mapa
* dificuldade das batalhas
* poder dos cavaleiros
* energia disponível de cada cavaleiro



# Estrutura do Projeto

```text
.
├── main.py
├── carregar_dados.py
├── busca_caminho.py
├── plano_batalha.py
├── interface.py
├── README.md
└── CSV's
    ├── mapa.csv
    ├── valor_terrenos.csv
    ├── poder_cavaleiro.csv
    ├── dificuldade_casa.csv
    └── legenda_terreno.csv
```

## Arquivos principais

### `main.py`

Arquivo responsável por **executar o programa**.

Funções principais:

* carregar os dados do problema
* executar o algoritmo de busca
* planejar as batalhas
* exibir os resultados
* iniciar a interface gráfica



### `carregar_dados.py`

Responsável por **ler os arquivos CSV** do projeto.

Funções disponíveis:

| Função                      | Descrição                                    |
| --------------------------- | -------------------------------------------- |
| `carregar_mapa`             | Carrega o mapa 42x42                         |
| `carregar_dicionario`       | Carrega dados chave→valor                    |
| `carregar_lista`            | Carrega lista de tuplas                      |
| `carregar_legenda_terrenos` | Relaciona código do mapa com nome do terreno |



### `busca_caminho.py`

Implementa o **algoritmo A*** para encontrar o melhor caminho no mapa.

Funções:

| Função                       | Descrição                    |
| ---------------------------- | ---------------------------- |
| `calcular_heuristica`        | Distância Manhattan          |
| `obter_vizinhos`             | Retorna movimentos possíveis |
| `calcular_caminho_a_estrela` | Executa o algoritmo A*       |


### `plano_batalha.py`

Responsável por **decidir quais cavaleiros lutarão em cada casa**.

O algoritmo:

1. gera todas as combinações possíveis de cavaleiros
2. calcula o tempo da batalha
3. escolhe a equipe mais rápida
4. atualiza a energia dos cavaleiros



### `interface.py`

Responsável por **visualizar o mapa e o caminho encontrado**.

Utiliza a biblioteca **Tkinter** para:

* desenhar o mapa
* colorir os terrenos
* animar o agente percorrendo o caminho



# Arquivos CSV

Os dados do problema são configuráveis por arquivos CSV.

### `mapa.csv`

Matriz **42 x 42** representando o terreno.

Valores possíveis:

| Código | Terreno    |
| ------ | ---------- |
| 14     | Plano      |
| 15     | Rochoso    |
| 16     | Montanhoso |


### `valor_terrenos.csv`

Define o custo de movimentação.

```text
Plano,1
Rochoso,5
Montanhoso,200
```



### `legenda_terreno.csv`

Relaciona código do mapa com o tipo de terreno.

```text
14,Plano
15,Rochoso
16,Montanhoso
```



### `poder_cavaleiro.csv`

Poder cósmico dos cavaleiros.

```text
Seiya,1.5
Shiryu,1.4
Hyoga,1.3
Shun,1.2
Ikki,1.1
```


### `dificuldade_casa.csv`

Dificuldade das casas do zodíaco.

```text
1,50
2,55
3,60
...
12,120
```


# Algoritmos Utilizados

## Algoritmo A*

O caminho no mapa é calculado usando **A***.

A função de avaliação é:

[
f(n) = g(n) + h(n)
]

Onde:

* **g(n)** = custo acumulado do caminho
* **h(n)** = heurística (distância Manhattan)

Heurística usada:

[
|x1-x2| + |y1-y2|
]

Isso permite encontrar o **caminho de menor custo** evitando terrenos muito caros.


# Planejamento de Batalhas

Para cada casa:

1. geramos todas as combinações possíveis de cavaleiros
2. verificamos se possuem energia
3. calculamos o tempo da batalha

Fórmula usada:

[
tempo = \frac{dificuldade}{\sum poder\ dos\ cavaleiros}
]

Após cada batalha:

```
energia_cavaleiro -= 1
```



# Interface Gráfica

A interface gráfica utiliza **Tkinter** para:

* desenhar o mapa
* representar diferentes terrenos
* animar o agente percorrendo o caminho

Cores utilizadas:

| Terreno    | Cor          |
| ---------- | ------------ |
| Plano      | cinza claro  |
| Rochoso    | cinza        |
| Montanhoso | cinza escuro |
| Caminho    | vermelho     |



# Como Executar o Projeto

## 1. Clonar ou baixar o projeto

```bash
git clone <repositorio>
```

ou baixar o ZIP.



## 2. Executar o programa

No terminal:

```bash
python main.py
```

ou

```bash
python3 main.py
```



# Saída Esperada

No terminal será exibido algo como:

```
Custo total do caminho: 1715

Casa: 1
Equipe: ('Shun', 'Ikki')
Tempo: 21.7

Casa: 2
Equipe: ('Shun', 'Ikki')
Tempo: 23.9

...

Tempo total de batalhas: 360
Energia restante: {'Seiya':0,'Shiryu':0,'Hyoga':0,'Shun':0,'Ikki':0}
```

Uma janela gráfica também será aberta mostrando o **agente percorrendo o mapa**.



# Tecnologias Utilizadas

* Python 3
* Tkinter
* CSV
* Algoritmo A*



# Conceitos de Inteligência Artificial Utilizados

* **Busca heurística**
* **Algoritmo A***
* **Planejamento de recursos**
* **Busca combinatória**

