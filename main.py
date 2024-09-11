
import numpy as np
import matplotlib.pyplot as plt
import random

def limpar(x, y):
  matriz_6x6[x][y] = 0

def movimentar(x, y, matriz_6x6):
  if matriz_6x6[x + 1][y] != 1:
    posAPAx += 1

def exibir(matriz):
    global posAPAx
    global posAPAy

    # Altera o esquema de cores do ambiente
    plt.imshow(matriz, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posAPAy] ,[posAPAx], marker='o', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()

def movimentar(x, y, matriz_6x6):
  if matriz_6x6[x + 1][y] != 1:
    posAPAx += 1

def sujar(matriz):
  posicoes_internas = [(i, j) for i in range(1, 5) for j in range(1, 5)]

  random.shuffle(posicoes_internas)

  num_valores = random.randint(1, len(posicoes_internas))

  for i in range(num_valores):
    pos = posicoes_internas[i]
    matriz[pos[0]][pos[1]] = 2

matriz_6x6 = [
    [1, 1, 1, 1, 1, 1],  # Primeira linha
    [1, 2, 0, 0, 0, 1],  # Segunda linha
    [1, 0, 0, 2, 0, 1],  # Terceira linha
    [1, 0, 0, 2, 3, 1],  # Quarta linha
    [1, 0, 0, 0, 0, 1],  # Quinta linha
    [1, 1, 1, 1, 1, 1]   # Última linha
]

posAPAx = 1
posAPAy = 1

sujar(matriz_6x6)

exibir(matriz_6x6)

while True:
  exibir(matriz_6x6)
  if matriz_6x6[posAPAx][posAPAy] == 2:
    limpar(posAPAx,posAPAy)
  movimentar(posAPAx, posAPAy, matriz_6x6)

# for y in range(1, 5):
#   posAPAy = y
#   for x in range(1,5):
#     posAPAx = x
#     if matriz_6x6[x][y] > 1:
#       limpar(x, y)
#     exibir(matriz_6x6)

# Função que exibe o ambiente na tela




