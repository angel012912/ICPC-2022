from re import I
from telnetlib import DM


def ganaJuego(dM, dJ, cC, sC):
    if dJ >= 23 or dM >= 23 or dM == 23 or dJ == 23 or dM > 13 or dJ > 13:
        return -1
    if dM <= dJ:
        if cantidadDeck(dM, cC):
            return dM
        return -1
    else:
        if cantidadDeck(dJ, cC):
            return dJ
        else: 
            answer = ganaJuego(dM, dJ + 1, cC, sC) 
    return answer

def suma(lista):
    c = 0
    for i in lista:
        if i >= 10:
            c += 10
        else:
            c += i
    return c

def cantidadDeck(n, cC):
    c = 0
    max = 3
    for i in cC:
        if (i == n):
            c += 1
    return (not(c > max)) 

if __name__ == '__main__':
    rondas = int(input())
    cJ = str(input())
    cJ = [int(x) for x in cJ.split()]
    cM = str(input())
    cM = [int(x) for x in cM.split()]
    cC = str(input())
    cC = [int(x) for x in cC.split()]

    sJ = suma(cJ)
    sM = suma(cM)
    sC = suma(cC)

    dM = 23 - (sM + sC)
    dJ = 24 - (sJ + sC)

    ct = cM + cJ + cC

    print(ganaJuego(dM, dJ, ct, sC))
