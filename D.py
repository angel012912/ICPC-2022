

from turtle import distance
from math import sqrt, pow, floor, ceil


def mid_point(posAct: list[int], vertice: list[int]):
    midpoint = [(posAct[0] + vertice[0]) / 2,(posAct[1] + vertice[1]) / 2]
    return midpoint


def euclidian_distance(destino: list[int], vertice: list[int]):
    b = pow((vertice[1] - destino[1]), 2)
    a = pow((vertice[0] - destino[0]), 2)
    c: float = (sqrt(a + b))
    return c


def particles(posAct, vertices, destino):
    if posAct == destino:
        return 0

    newStart = []
    distances = []
    for atractor in vertices:
        newStart.append(mid_point(posAct, atractor))

    for vertex in newStart:
        distances.append(euclidian_distance(destino, vertex))
    min = 0
    for i in range(1, len(distances)):
        if distances[min] > distances[i]:
            min = i
    activ = particles(newStart[min], vertices, destino)

    return activ + 1



if __name__ == '__main__':
    numeros = str(input())
    numeros = [int(x) for x in numeros.split()]
    n: int = numeros[0]
    x: int = numeros[1]
    y: int = numeros[2]


    posAct = [2 ** (n - 1), 2 ** (n - 1)]
    vertices = [[0, 0], [0, 2 ** n], [2 ** n, 0], [2 ** n, 2 ** n]]
    destino = [x, y]
    print(particles(posAct, vertices, destino))