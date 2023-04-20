from typing import List


def deleteBaloon(listaGlobos: list):
    r:List[List] = []
    for g in numeros:
        if not r :
            r.append([g])
        else:
            enc = False
            for n in r:
                if n[-1] - g == 1:
                    n.append(g)
                    enc = True
                    break
            if not enc:
                r.append([g])
    return (len(r))

if __name__ == '__main__':
    n = int(input())
    numeros = str(input())
    numeros = [int(x) for x in numeros.split()]
    print(deleteBaloon(numeros))
   