
# 🛡️ Cavaleiros do Zodíaco — Agente de Busca para as 12 Casas

## 📖 Descrição

Durante o torneio da Guerra Galáctica, os Cavaleiros de Bronze descobrem que Saori é a reencarnação da deusa Atena e que o Grande Mestre tentou assassiná-la quando ainda era bebê. Decididos a protegê-la, Seiya, Shiryu, Hyoga, Shun e Ikki partem rumo ao Santuário para enfrentar o Grande Mestre.

Ao chegar ao Santuário, Tremy, um Cavaleiro de Prata, ataca o grupo e acerta Atena com uma flecha mortal.

Para salvá-la, os Cavaleiros precisam:

- Percorrer as 12 Casas do Zodíaco
- Derrotar os 12 Cavaleiros de Ouro
- Chegar até a Casa do Grande Mestre
- Fazer tudo isso em até 12 horas

O objetivo deste projeto é implementar um agente inteligente capaz de planejar automaticamente a melhor estratégia para atravessar as 12 casas e salvar Atena no menor tempo possível.

## 🎯 Objetivo do Projeto

Desenvolver um agente autônomo que:

- Encontre o melhor caminho pelo mapa
- Planeje quais cavaleiros lutarão em cada batalha
- Minimize o tempo total da missão

Para isso, deve ser utilizado um algoritmo de busca estudado na disciplina de Inteligência Artificial.

## 🗺️ Mapa das 12 Casas

O mapa do Santuário é representado por uma matriz 42 × 42 contendo diferentes tipos de terreno.

Tipos de terreno:

| Terreno | Custo de tempo |
|-------|------|
| Montanhoso | +200 minutos |
| Plano | +1 minuto |
| Rochoso | +5 minutos |

Regras de movimentação:

- O agente não pode andar na diagonal
- Apenas movimentos verticais e horizontais
- Início: Entrada do Santuário (vermelho)
- Objetivo final: Casa do Grande Mestre (verde)

## 🏛️ Dificuldade das Casas do Zodíaco

Cada casa possui um nível de dificuldade, que influencia o tempo da batalha.

| Casa | Dificuldade |
|----|----|
| Áries | 50 |
| Touro | 55 |
| Gêmeos | 60 |
| Câncer | 70 |
| Leão | 75 |
| Virgem | 80 |
| Libra | 85 |
| Escorpião | 90 |
| Sagitário | 95 |
| Capricórnio | 100 |
| Aquário | 110 |
| Peixes | 120 |

## ⚡ Cavaleiros de Bronze

Cada cavaleiro possui um poder cósmico, que influencia o tempo de batalha.

| Cavaleiro | Poder Cósmico |
|----|----|
| Seiya | 1.5 |
| Shiryu | 1.4 |
| Hyoga | 1.3 |
| Shun | 1.2 |
| Ikki | 1.1 |

Todos os cavaleiros começam com:

- 5 pontos de energia

Regras:

- Cada batalha consome 1 ponto de energia
- Se a energia chegar a 0, o cavaleiro morre

## ⏱️ Tempo das Batalhas

O tempo para derrotar um Cavaleiro de Ouro é calculado por:

Tempo = Dificuldade da Casa / (Soma do poder cósmico dos cavaleiros participantes)

Quanto mais cavaleiros participarem da batalha, menor será o tempo necessário.

## 🧠 Problemas a Resolver

O trabalho possui dois problemas principais.

### 1️⃣ Planejamento de Caminho

Encontrar a rota ótima no mapa até a casa do Grande Mestre.

Possíveis algoritmos:

- A*
- Dijkstra
- BFS
- UCS

### 2️⃣ Planejamento de Batalhas

Determinar quais cavaleiros lutarão em cada casa, considerando:

- Poder cósmico
- Energia restante
- Tempo total da missão

## ⚙️ Requisitos do Sistema

O programa deve:

- Utilizar algoritmo de busca
- Representar o mapa como matriz 42x42
- Permitir edição do mapa
- Permitir configuração das casas
- Permitir configuração dos cavaleiros
- Mostrar visualização dos movimentos do agente

Pode ser:

- Interface gráfica simples
- Ou visualização no console

## 📊 Saída Esperada

Ao final da execução o programa deve mostrar:

- Caminho percorrido pelo agente
- Custo total do caminho
- Equipe escolhida para cada batalha
- Tempo gasto em cada casa
- Tempo total da missão

## 💻 Tecnologias

O projeto pode ser implementado em qualquer linguagem de programação.

Exemplos comuns:

- Python
- Java
- C++
- JavaScript

## 🎥 Apresentação (Pitch)

Os alunos devem gravar um vídeo curto apresentando o projeto.

Estrutura recomendada:

### 1. Apresentação
Quem são os integrantes do grupo.

### 2. Contexto do problema
Explicar o desafio das 12 casas do Zodíaco.

### 3. Solução proposta
Explicar:

- Algoritmo utilizado
- Estrutura da solução

### 4. Demonstração
Mostrar o programa executando.

### 5. Conclusão
Agradecimento e menção à disciplina.

Duração: 30 segundos a 5 minutos.

## 📋 Critérios de Avaliação

O trabalho será avaliado considerando:

- Atendimento aos requisitos
- Implementação correta dos algoritmos
- Organização do código
- Qualidade da apresentação
- Adequação do método escolhido

## ⭐ Bônus

### Interface Gráfica
Implementar uma interface 2D ou 3D pode render:

+1 ponto

### Melhor desempenho
A solução que encontrar a melhor resposta com menor tempo de execução ganha:

+1 ponto

## 🏁 Resultado Esperado

Ao final, o agente deve conseguir:

✔ Percorrer as 12 casas do Zodíaco  
✔ Derrotar os 12 Cavaleiros de Ouro  
✔ Chegar à Casa do Grande Mestre  
✔ Salvar Atena dentro de 12 horas