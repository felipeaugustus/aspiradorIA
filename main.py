import matplotlib.pyplot as plt
import random

# Matriz inicial
matriz_6x6 = [
    [1, 1, 1, 1, 1, 1],  # Primeira linha
    [1, 0, 0, 0, 0, 1],  # Segunda linha
    [1, 0, 0, 0, 0, 1],  # Terceira linha
    [1, 0, 0, 0, 0, 1],  # Quarta linha
    [1, 0, 0, 0, 0, 1],  # Quinta linha
    [1, 1, 1, 1, 1, 1]  # Última linha
]

posAPAx = 1
posAPAy = 1


def sujar(matriz):
    posicoes_internas = [(i, j) for i in range(1, 5) for j in range(1, 5)]
    random.shuffle(posicoes_internas)
    num_valores = random.randint(1, len(posicoes_internas))
    for i in range(num_valores):
        pos = posicoes_internas[i]
        matriz[pos[0]][pos[1]] = 2


def exibir(matriz):
    global posAPAx, posAPAy
    plt.imshow(matriz, cmap='gray', vmin=0, vmax=3)
    plt.plot([posAPAx], [posAPAy], marker='o', color='r', ls='')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()


def limpar(x, y):
    matriz_6x6[y][x] = 0


direcao = "direita"


def movimentar(matriz):
    global posAPAx, posAPAy, direcao

    if posAPAx == len(matriz[posAPAy]) - 2:
        direcao = "esquerda"
    elif posAPAx == 1:
        direcao = "direita"

    if posAPAx % 2 != 0:
        if matriz[posAPAy + 1][posAPAx] != 1:
            return "abaixo"
        elif direcao == "direita":
            return "direita"
        else:
            return "esquerda"
    else:
        if matriz[posAPAy - 1][posAPAx] != 1:
            return "acima"
        return direcao


sujar(matriz_6x6)


def agenteReativoSimples(percepcao):
    global posAPAx, posAPAy, direcao

    if percepcao['sujo'] == 2:
        return "aspirar"

    if percepcao['x'] == len(matriz_6x6[percepcao['y']]) - 2:
        direcao = "esquerda"
    elif percepcao['x'] == 1:
        direcao = "direita"

    if percepcao['x'] % 2 != 0:
        if matriz_6x6[percepcao['y'] + 1][percepcao['x']] != 1:
            return "abaixo"
        elif direcao == "direita":
            return "direita"
        else:
            return "esquerda"
    else:
        if matriz_6x6[percepcao['y'] - 1][percepcao['x']] != 1:
            return "acima"
        return direcao


def realizarAcao(acao):
    global posAPAx, posAPAy
    if acao == "aspirar":
        limpar(posAPAx, posAPAy)
    elif acao == "direita":
        posAPAx += 1
    elif acao == "esquerda":
        posAPAx -= 1
    elif acao == "abaixo":
        posAPAy += 1
    elif acao == "acima":
        posAPAy -= 1


while True:
    exibir(matriz_6x6)
    x = posAPAx
    y = posAPAy
    sujo = matriz_6x6[y][x]
    percep = {'x': x, 'y': y, 'sujo': sujo}
    realizarAcao(agenteReativoSimples(percep))


